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
        self.board = [None] * 9
        self.turn_timestamps = [None] * 9
        self.current_turn = None
        self.game_finished = False

    def StartGame(self, request, context):
        #retrive current state of node
        ids = request.list_ids
        #if node port in list -> loop is completed and we can select a leader
        if node_id in ids:
            leader_id = max(ids)
            print(f"Ring is complete. Choosing leader {leader_id}")
            leader_time = datetime.utcnow().isoformat()
            response = node_pb2.ElectionResponse(leader_id=leader_id, leader_time=leader_time)
            if self.node_id != self.leader_id:
                Main.leader_id = response.leader_id
            return response

        else:
            #if not -> we append the port of the current node to the list. Pass this list to the next node.
            ids.append(node_id)
            print("Collected current ID. Moving to the next node ....")
            next_node_id = (self.node_id + 1) % 3
            #connecting to the next node, pass the list of ids
            response = self.stubs[next_node_id].StartGame(node_pb2.InitParams(list_ids=ids))
            if self.node_id != self.leader_id:
                Main.leader_id = response.leader_id
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
        timestamp = datetime.utcnow() + self.clock_adjust
        print(f"Symbol set request {request.type} at time {timestamp}")
        if self.board[request.pos] is not None:
            return node_pb2.SymbolResponse(isComplete=False, message='Position is occupied, choose a different one.')
        if request.type not in {'X', 'O'}:
            return node_pb2.SymbolResponse(isComplete=False, message=f'Invalid symbol specified. Supported are X or O. You provided: {request.type}')
        if self.current_turn is not None and self.current_turn != request.type:
            return node_pb2.SymbolResponse(isComplete=False, message=f'It\'s not your turn, please wait for the opponent ({self.current_turn}) to make a move.')
        self.turn_timestamps[request.pos] = timestamp
        self.board[request.pos] = request.type
        self.current_turn = 'X' if request.type == 'O' else 'O'
        print('Updated the board:', self._format_board())
        if self._check_winner(request.type):
            # todo: reset game here
            self.game_finished = True
            return node_pb2.SymbolResponse(isComplete=True, message='Congratulations, you won!')
        return node_pb2.SymbolResponse(isComplete=True, message='You made your turn.')

    def _check_winner(self, type):
        rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        cols = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        diagonals = [[0, 4, 8], [2, 4, 6]]
        if any(all(self.board[i] == type for i in seq) for seq in rows):
            print('Winner by rows.')
            return True
        if any(all(self.board[i] == type for i in seq) for seq in cols):
            print('Winner by cols.')
            return True
        if any(all(self.board[i] == type for i in seq) for seq in diagonals):
            print('Winner by diagonals.')
            return True

    def ListBoard(self, request, context):
        return node_pb2.BoardResponse(board=self._format_board(), isComplete=self.game_finished)

    def _format_board(self):
        return ', '.join((self.board[i] + ':' + str(self.turn_timestamps[i]) if self.board[i] else 'empty') for i in range(9))


class Main(cmd.Cmd):
    prompt = '> '
    leader_id = None
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
        print(args)
        position = args[0]
        symbol = args[2]
        request = node_pb2.Symbol(pos=int(position), type=symbol, node_id=0, node_time='')
        response = self.stubs[Main.leader_id].SetSymbol(request)
        if not response.isComplete:
            print(f"Unable to make a move: {response.message}")
        else:
            print('Placed a symbol:', response.message)

    def do_List_board(self, args):
        if self.leader_id is None:
            print('Game is not started. Leader id is unknown')
            return
        response = self.stubs[Main.leader_id].ListBoard(node_pb2.Empty())
        print(f'Game is finished: {response.isComplete}. Board: {response.board}')
        return response

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
