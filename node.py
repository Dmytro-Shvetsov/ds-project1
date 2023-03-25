import cmd
import node_pb2
import node_pb2_grpc
import threading
import grpc
import time
from concurrent import futures
import sys
import datetime 

BASE_PORT = 50060

class TicTacToeServicer(node_pb2_grpc.TicTacToeServicer):
    def __init__(self, node_id) -> None:
        self.node_id = node_id

    def StartGame(self, request, context):
        n_nodes = request.n_nodes
        node_id = request.node_id
        node_time = request.node_time
        isLeader = request.isLeader
        ids = request.list_ids

        if node_id in ids:
            print("Ring is complete. Choosing leader ....")
            leader_id = max(ids)
            isLeader = True
            leader_time = datetime.datetime.utcnow().isoformat()
            n_players = 2
            for i in range(n_players):
                with grpc.insecure_channel(f"localhost:{(leader_id + i - BASE_PORT + 1) % n_nodes + BASE_PORT}"):
                     return node_pb2.ElectionResponse(leader_id= leader_id, isComplete = isLeader, leader_time= leader_time)
        
        if node_id not in ids:
            ids.append(node_id)
            isLeader = False
            print("Collected current ID. Moving to the next node ....")
            next_node_id = (node_id - BASE_PORT + 1) % n_nodes + BASE_PORT
            with grpc.insecure_channel(f"localhost:{next_node_id}") as channel:
                stub = node_pb2_grpc.RingElectionStub(channel)
                response = stub.Election(node_pb2.InitParams(n_nodes= n_nodes, 
                                                             node_id= next_node_id, 
                                                             node_time= node_time, 
                                                             isLeader= isLeader,
                                                             list_ids=ids))
                return response

class Main(cmd.Cmd):
    prompt = '> '

    def __init__(self, node_id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.node_id = node_id
        self.prompt = f'Node-{node_id}> '

        self.channel = grpc.insecure_channel(f"localhost:{BASE_PORT + 1}")
        self.stub = node_pb2_grpc.TicTacToeStub(self.channel)

    def do_Start_game(self, args):
        with grpc.insecure_channel(f"localhost:{BASE_PORT + 1}") as channel:
            stub = node_pb2_grpc.TicTacToeStub(channel)
            request = node_pb2.InitParams(n_nodes=0, node_id=0, node_time='', isLeader=True, list_ids=[])
            response = stub.StartGame(request)
            print("Game started")
            return response
        request = node_pb2.InitParams(n_nodes=0, node_id=0,node_time='', isLeader=True, list_ids=[])
        response = self.stub.StartGame(request)
        print("Game started")
        return response

    def do_Set_symbol(self, args):
        print("Symbol set")

    def do_List_board(self, args):
        print("Board listed")

    def do_Set_node_time(self, args):
        print("Node time set")

    def do_Set_time_out(self, args):
        print("Timeout set")


if __name__ == '__main__':
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
            print(exc)
            server.stop(0)
    