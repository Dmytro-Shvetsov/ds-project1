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
        self.NotifyLeader = channel.unary_unary(
                '/TicTacToe/NotifyLeader',
                request_serializer=node__pb2.LeaderID.SerializeToString,
                response_deserializer=node__pb2.SuccessResponse.FromString,
                )
        self.SetSymbol = channel.unary_unary(
                '/TicTacToe/SetSymbol',
                request_serializer=node__pb2.Symbol.SerializeToString,
                response_deserializer=node__pb2.SymbolResponse.FromString,
                )
        self.ListBoard = channel.unary_unary(
                '/TicTacToe/ListBoard',
                request_serializer=node__pb2.Empty.SerializeToString,
                response_deserializer=node__pb2.BoardResponse.FromString,
                )
        self.SetLeader = channel.unary_unary(
                '/TicTacToe/SetLeader',
                request_serializer=node__pb2.Leader.SerializeToString,
                response_deserializer=node__pb2.LeaderResponse.FromString,
                )
        self.RequestTime = channel.unary_unary(
                '/TicTacToe/RequestTime',
                request_serializer=node__pb2.Empty.SerializeToString,
                response_deserializer=node__pb2.NodeTime.FromString,
                )
        self.SetTimeDiff = channel.unary_unary(
                '/TicTacToe/SetTimeDiff',
                request_serializer=node__pb2.TimeDiff.SerializeToString,
                response_deserializer=node__pb2.Empty.FromString,
                )
        self.NotifyWinner = channel.unary_unary(
                '/TicTacToe/NotifyWinner',
                request_serializer=node__pb2.Winner.SerializeToString,
                response_deserializer=node__pb2.Empty.FromString,
                )
        self.NotifyTimeout = channel.unary_unary(
                '/TicTacToe/NotifyTimeout',
                request_serializer=node__pb2.TimeoutMessage.SerializeToString,
                response_deserializer=node__pb2.Empty.FromString,
                )
        self.SetTimeoutTime = channel.unary_unary(
                '/TicTacToe/SetTimeoutTime',
                request_serializer=node__pb2.TimeoutSetRequest.SerializeToString,
                response_deserializer=node__pb2.TimeoutMessage.FromString,
                )


class TicTacToeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifyLeader(self, request, context):
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

    def SetLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTimeDiff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifyWinner(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifyTimeout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTimeoutTime(self, request, context):
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
            'NotifyLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyLeader,
                    request_deserializer=node__pb2.LeaderID.FromString,
                    response_serializer=node__pb2.SuccessResponse.SerializeToString,
            ),
            'SetSymbol': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSymbol,
                    request_deserializer=node__pb2.Symbol.FromString,
                    response_serializer=node__pb2.SymbolResponse.SerializeToString,
            ),
            'ListBoard': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBoard,
                    request_deserializer=node__pb2.Empty.FromString,
                    response_serializer=node__pb2.BoardResponse.SerializeToString,
            ),
            'SetLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLeader,
                    request_deserializer=node__pb2.Leader.FromString,
                    response_serializer=node__pb2.LeaderResponse.SerializeToString,
            ),
            'RequestTime': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestTime,
                    request_deserializer=node__pb2.Empty.FromString,
                    response_serializer=node__pb2.NodeTime.SerializeToString,
            ),
            'SetTimeDiff': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTimeDiff,
                    request_deserializer=node__pb2.TimeDiff.FromString,
                    response_serializer=node__pb2.Empty.SerializeToString,
            ),
            'NotifyWinner': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyWinner,
                    request_deserializer=node__pb2.Winner.FromString,
                    response_serializer=node__pb2.Empty.SerializeToString,
            ),
            'NotifyTimeout': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyTimeout,
                    request_deserializer=node__pb2.TimeoutMessage.FromString,
                    response_serializer=node__pb2.Empty.SerializeToString,
            ),
            'SetTimeoutTime': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTimeoutTime,
                    request_deserializer=node__pb2.TimeoutSetRequest.FromString,
                    response_serializer=node__pb2.TimeoutMessage.SerializeToString,
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
    def NotifyLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/NotifyLeader',
            node__pb2.LeaderID.SerializeToString,
            node__pb2.SuccessResponse.FromString,
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
            node__pb2.Empty.SerializeToString,
            node__pb2.BoardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/SetLeader',
            node__pb2.Leader.SerializeToString,
            node__pb2.LeaderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/RequestTime',
            node__pb2.Empty.SerializeToString,
            node__pb2.NodeTime.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetTimeDiff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/SetTimeDiff',
            node__pb2.TimeDiff.SerializeToString,
            node__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifyWinner(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/NotifyWinner',
            node__pb2.Winner.SerializeToString,
            node__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifyTimeout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/NotifyTimeout',
            node__pb2.TimeoutMessage.SerializeToString,
            node__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetTimeoutTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TicTacToe/SetTimeoutTime',
            node__pb2.TimeoutSetRequest.SerializeToString,
            node__pb2.TimeoutMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
