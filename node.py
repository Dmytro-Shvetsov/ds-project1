import cmd
import node_pb2
import node_pb2_grpc
import threading
import grpc
import time
from concurrent import futures
import sys
import time
from datetime import datetime, timedelta

BASE_PORT = 50051

class TicTacToeServicer(node_pb2_grpc.TicTacToeServicer):
    def __init__(self, node_id) -> None:
        self.node_id = node_id
        self.leader_id = None
        self.channels = {i:grpc.insecure_channel(f"localhost:{BASE_PORT + i}") for i in range(3) if i != node_id}
        self.stubs = {i:node_pb2_grpc.TicTacToeStub(self.channels[i]) for i in range(3) if i != node_id}
        self.clock_adjust = timedelta(0)

    def StartGame(self, request, context):
        #retrive current state of node
        ids = request.list_ids
        #if node port in list -> loop is completed and we can select a leader
        if node_id in ids:
            leader_id = max(ids)
            print(f"Ring is complete. Choosing leader {leader_id}")
            leader_time = datetime.utcnow().isoformat()
            return node_pb2.ElectionResponse(leader_id=leader_id, leader_time=leader_time)
        else:
            #if not -> we append the port of the current node to the list. Pass this list to the next node.
            ids.append(node_id)
            print("Collected current ID. Moving to the next node ....")
            next_node_id = (self.node_id + 1) % 3
            #connecting to the next node, pass the list of ids
            response = self.stubs[next_node_id].StartGame(node_pb2.InitParams(list_ids=ids))
            return response

    def NotifyLeader(self, request, context):
        self.leader_id = request.leader_id
        print(f"I know that leader id is {self.leader_id}")
        if self.leader_id == self.node_id:
            self.synchronize_clocks()

        return node_pb2.SuccessResponse(isComplete=True)

    def RequestTime(self, request, context):
        return node_pb2.NodeTime(node_time=(datetime.utcnow() + self.clock_adjust).isoformat(), node_id=self.node_id)

    def SetTimeDiff(self, request, context):
        self.clock_adjust = timedelta(seconds=request.total_time_seconds)
        print(f'#{self.node_id} synchronizing time with the server. Time diff seconds: {self.clock_adjust.total_seconds()}')
        return node_pb2.Empty()

    def synchronize_clocks(self):
        diffs = self._get_time_diffs()
        average_diff = sum(diffs, timedelta(0)).total_seconds() / len(diffs)
        for i, stub in self.stubs.items():
            print(f'Synchronizing time of node {i}. Time diff: {average_diff}')
            stub.SetTimeDiff(node_pb2.TimeDiff(total_time_seconds=average_diff))

    def _get_time_diffs(self):
        diffs = []
        for i in range(3):
            if i == self.node_id:
                continue
            now = datetime.utcnow()
            start_clock = time.perf_counter()
            dest_time = self.stubs[i].RequestTime(node_pb2.Empty())
            rtt = time.perf_counter() - start_clock
            diff = now - datetime.fromisoformat(dest_time.node_time) + timedelta(seconds=(rtt / 2))
            print(f'Time difference with node {i}: {diff.total_seconds()}')
            diffs.append(diff)
        return diffs

    def SetSymbol(self, request, context):
        print("symbol set", request)
        return node_pb2.SymbolResponse(isComplete=True)


class Main(cmd.Cmd):
    prompt = '> '

    def __init__(self, node_id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.node_id = node_id
        self.prompt = f'Node-{node_id}> '
        self.channels = {i:grpc.insecure_channel(f"localhost:{BASE_PORT + i}") for i in range(3)}
        self.stubs = {i:node_pb2_grpc.TicTacToeStub(self.channels[i]) for i in range(3)}

    def do_Start_game(self, args):
        #After we Start_game, connect to the BASE_PORT(50060)(to yourself) and initiate election
        request = node_pb2.InitParams(list_ids=[])
        response = self.stubs[self.node_id].StartGame(request)
        #When the circle is completed, present a new leader
        print(f"Now I know that the leader is {response.leader_id}. Leader time is {response.leader_time}")
        print("Game started")

        for k, v in self.stubs.items():
            v.NotifyLeader(node_pb2.LeaderID(leader_id=response.leader_id))
        return response

    def do_Set_symbol(self, args):
        position = args[0]
        symbol = args[2]
        request = node_pb2.Symbol(pos=int(position), type=symbol, node_id=0, node_time='')
        response = self.stub.SetSymbol(request)
        print(response)

    def do_List_board(self, args):
        print("Board listed")

    def do_Set_node_time(self, args):
        print("Node time set")

    def do_Set_time_out(self, args):
        print("Timeout set")


if __name__ == '__main__':
    #Creating 3 nodes with ports 50060 50061 50062
    node_id = int(sys.argv[1])
    run_port = BASE_PORT + node_id
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    node_pb2_grpc.add_TicTacToeServicer_to_server(TicTacToeServicer(node_id), server)
    server.add_insecure_port(f'[::]:{run_port}')
    server.start()
    print(f"Node started on port {run_port}")
    
    cli = Main(node_id)
    while True:
        try:
            cli.cmdloop()
        except Exception as exc:
            server.stop(0)
            raise exc
