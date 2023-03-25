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
        #retrive current state of node
        n_nodes = request.n_nodes
        node_id = request.node_id
        node_time = request.node_time
        isLeader = request.isLeader
        ids = request.list_ids
        #if node port in list -> loop is completed and we can select a leader
        if node_id in ids:
            print("Ring is complete. Choosing leader ....")
            leader_id = max(ids)
            print(f"Leader is on port {leader_id}")
            isLeader = True
            leader_time = datetime.datetime.utcnow().isoformat()
            return node_pb2.ElectionResponse(leader_id= leader_id, isComplete = isLeader, leader_time= leader_time)
        #if not -> we append the port of the current node to the list. Pass this list to the next node.
        if node_id not in ids:
            ids.append(node_id)
            isLeader = False
            print("Collected current ID. Moving to the next node ....")
            next_node_id = (node_id - BASE_PORT + 1) % n_nodes + BASE_PORT
            #connecting to the next node, pass the list of ids
            with grpc.insecure_channel(f"localhost:{next_node_id}") as channel:
                stub = node_pb2_grpc.TicTacToeStub(channel)
                response = stub.StartGame(node_pb2.InitParams(n_nodes= n_nodes, 
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
        self.node_port = BASE_PORT + node_id

        self.channel = grpc.insecure_channel(f"localhost:{BASE_PORT + 1}")
        self.stub = node_pb2_grpc.TicTacToeStub(self.channel)

    def do_Start_game(self, args):
        #After we Start_game, connect to the BASE_PORT(50060)(to yourself) and initiate election
        with grpc.insecure_channel(f"localhost:{self.node_port}") as channel:
            stub = node_pb2_grpc.TicTacToeStub(channel)
            request = node_pb2.InitParams(n_nodes=3, node_id=self.node_port, node_time='', isLeader=False, list_ids=[])
            response = stub.StartGame(request)
            #When the circle is completed, present a new leader
            if response.isComplete == True:
                print(f"Now I know that the leader is {response.leader_id}")
                print(f"Leader time is {response.leader_time}")
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
            print(exc)
            server.stop(0)
    