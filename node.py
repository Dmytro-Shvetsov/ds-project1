import cmd
import node_pb2
import node_pb2_grpc
import threading
import grpc
import time
from concurrent import futures
import sys

BASE_PORT = 50060

class TicTacToeServicer(node_pb2_grpc.TicTacToeServicer):
    def StartGame(self, request, context):
        print("game started", request)
        return node_pb2.ElectionResponse(leader_id=0, isComplete=True, leader_time='')


class Main(cmd.Cmd):
    prompt = '> '

    def __init__(self, node_id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.node_id = node_id
        self.prompt = f'Node-{node_id}> '

    def do_Start_game(self, args):
        with grpc.insecure_channel(f"localhost:{BASE_PORT + 1}") as channel:
            stub = node_pb2_grpc.TicTacToeStub(channel)
            request = node_pb2.InitParams(n_nodes=0, node_id=0,node_time='', isLeader=True, list_ids=[])
            response = stub.StartGame(request)
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
    node_pb2_grpc.add_TicTacToeServicer_to_server(TicTacToeServicer(), server)
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
    