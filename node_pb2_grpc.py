# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import node_pb2 as node__pb2


class TicTacToeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartGame = channel.unary_unary(
                '/TicTacToe/StartGame',
                request_serializer=node__pb2.InitParams.SerializeToString,
                response_deserializer=node__pb2.ElectionResponse.FromString,
                )
        self.SetSymbol = channel.unary_unary(
                '/TicTacToe/SetSymbol',
                request_serializer=node__pb2.Symbol.SerializeToString,
                response_deserializer=node__pb2.SymbolResponse.FromString,
                )
        self.ListBoard = channel.unary_unary(
                '/TicTacToe/ListBoard',
                request_serializer=node__pb2.Board.SerializeToString,
                response_deserializer=node__pb2.BoardResponse.FromString,
                )
        self.SetNodeTime = channel.unary_unary(
                '/TicTacToe/SetNodeTime',
                request_serializer=node__pb2.NodeTime.SerializeToString,
                response_deserializer=node__pb2.NodeTimeResponse.FromString,
                )


class TicTacToeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSymbol(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBoard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetNodeTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TicTacToeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartGame': grpc.unary_unary_rpc_method_handler(
                    servicer.StartGame,
                    request_deserializer=node__pb2.InitParams.FromString,
                    response_serializer=node__pb2.ElectionResponse.SerializeToString,
            ),
            'SetSymbol': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSymbol,
                    request_deserializer=node__pb2.Symbol.FromString,
                    response_serializer=node__pb2.SymbolResponse.SerializeToString,
            ),
            'ListBoard': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBoard,
                    request_deserializer=node__pb2.Board.FromString,
                    response_serializer=node__pb2.BoardResponse.SerializeToString,
            ),
            'SetNodeTime': grpc.unary_unary_rpc_method_handler(
                    servicer.SetNodeTime,
                    request_deserializer=node__pb2.NodeTime.FromString,
                    response_serializer=node__pb2.NodeTimeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TicTacToe', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TicTacToe(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/StartGame',
            node__pb2.InitParams.SerializeToString,
            node__pb2.ElectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSymbol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/SetSymbol',
            node__pb2.Symbol.SerializeToString,
            node__pb2.SymbolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBoard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/ListBoard',
            node__pb2.Board.SerializeToString,
            node__pb2.BoardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetNodeTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/SetNodeTime',
            node__pb2.NodeTime.SerializeToString,
            node__pb2.NodeTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
