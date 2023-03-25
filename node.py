import cmd
import tictactoe_pb2
import tictactoe_pb2_grpc
import threading
import grpc
import time
from concurrent import futures
import sys

global stub


class TicTacToeServicer(tictactoe_pb2_grpc.TicTacToeServiceServicer):
    def StartGame(self, request, context):
        print("game started")

        return tictactoe_pb2.QuickSortResponse()

class Main(cmd.Cmd):
    prompt = '> '


    def do_Start_game(self, args):
        request = tictactoe_pb2.StartGameRequest()
        response = stub.StartGame(request)
        print("Game started")

    def do_Set_symbol(self, args):
        print("Symbol set")

    def do_List_board(self, args):
        print("Board listed")

    def do_Set_node_time(self, args):
        print("Node time set")

    def do_Set_time_out(self, args):
        print("Timeout set")

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tictactoe_pb2_grpc.add_TicTacToeServiceServicer_to_server(TicTacToeServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started, CONNECTED to port {port}")

if __name__ == '__main__':
    run_port = sys.argv[1]
    target_port = sys.argv[2]
    channel = grpc.insecure_channel(f"localhost:{run_port}")
    stub = tictactoe_pb2_grpc.TicTacToeServiceStub(channel)
    print(f"Node started on port {run_port}")
    serve(int(target_port))
    cli = Main()
    cli.cmdloop()