# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service_pb2 as service__pb2


class GameStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPlayerActions = channel.unary_unary(
                '/protos.Game/GetPlayerActions',
                request_serializer=service__pb2.State.SerializeToString,
                response_deserializer=service__pb2.PlayerActions.FromString,
                )
        self.GetCoachActions = channel.unary_unary(
                '/protos.Game/GetCoachActions',
                request_serializer=service__pb2.State.SerializeToString,
                response_deserializer=service__pb2.CoachActions.FromString,
                )
        self.GetTrainerActions = channel.unary_unary(
                '/protos.Game/GetTrainerActions',
                request_serializer=service__pb2.State.SerializeToString,
                response_deserializer=service__pb2.TrainerActions.FromString,
                )
        self.SendInitMessage = channel.unary_unary(
                '/protos.Game/SendInitMessage',
                request_serializer=service__pb2.InitMessage.SerializeToString,
                response_deserializer=service__pb2.Empty.FromString,
                )
        self.SendServerParams = channel.unary_unary(
                '/protos.Game/SendServerParams',
                request_serializer=service__pb2.ServerParam.SerializeToString,
                response_deserializer=service__pb2.Empty.FromString,
                )
        self.SendPlayerParams = channel.unary_unary(
                '/protos.Game/SendPlayerParams',
                request_serializer=service__pb2.PlayerParam.SerializeToString,
                response_deserializer=service__pb2.Empty.FromString,
                )
        self.SendPlayerType = channel.unary_unary(
                '/protos.Game/SendPlayerType',
                request_serializer=service__pb2.PlayerType.SerializeToString,
                response_deserializer=service__pb2.Empty.FromString,
                )
        self.GetInitMessage = channel.unary_unary(
                '/protos.Game/GetInitMessage',
                request_serializer=service__pb2.Empty.SerializeToString,
                response_deserializer=service__pb2.InitMessageFromServer.FromString,
                )
        self.SendByeCommand = channel.unary_unary(
                '/protos.Game/SendByeCommand',
                request_serializer=service__pb2.Empty.SerializeToString,
                response_deserializer=service__pb2.Empty.FromString,
                )


class GameServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPlayerActions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCoachActions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrainerActions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendInitMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendServerParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPlayerParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPlayerType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInitMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendByeCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPlayerActions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayerActions,
                    request_deserializer=service__pb2.State.FromString,
                    response_serializer=service__pb2.PlayerActions.SerializeToString,
            ),
            'GetCoachActions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCoachActions,
                    request_deserializer=service__pb2.State.FromString,
                    response_serializer=service__pb2.CoachActions.SerializeToString,
            ),
            'GetTrainerActions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrainerActions,
                    request_deserializer=service__pb2.State.FromString,
                    response_serializer=service__pb2.TrainerActions.SerializeToString,
            ),
            'SendInitMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendInitMessage,
                    request_deserializer=service__pb2.InitMessage.FromString,
                    response_serializer=service__pb2.Empty.SerializeToString,
            ),
            'SendServerParams': grpc.unary_unary_rpc_method_handler(
                    servicer.SendServerParams,
                    request_deserializer=service__pb2.ServerParam.FromString,
                    response_serializer=service__pb2.Empty.SerializeToString,
            ),
            'SendPlayerParams': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPlayerParams,
                    request_deserializer=service__pb2.PlayerParam.FromString,
                    response_serializer=service__pb2.Empty.SerializeToString,
            ),
            'SendPlayerType': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPlayerType,
                    request_deserializer=service__pb2.PlayerType.FromString,
                    response_serializer=service__pb2.Empty.SerializeToString,
            ),
            'GetInitMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInitMessage,
                    request_deserializer=service__pb2.Empty.FromString,
                    response_serializer=service__pb2.InitMessageFromServer.SerializeToString,
            ),
            'SendByeCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendByeCommand,
                    request_deserializer=service__pb2.Empty.FromString,
                    response_serializer=service__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.Game', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Game(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPlayerActions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/GetPlayerActions',
            service__pb2.State.SerializeToString,
            service__pb2.PlayerActions.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCoachActions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/GetCoachActions',
            service__pb2.State.SerializeToString,
            service__pb2.CoachActions.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrainerActions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/GetTrainerActions',
            service__pb2.State.SerializeToString,
            service__pb2.TrainerActions.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendInitMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/SendInitMessage',
            service__pb2.InitMessage.SerializeToString,
            service__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendServerParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/SendServerParams',
            service__pb2.ServerParam.SerializeToString,
            service__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPlayerParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/SendPlayerParams',
            service__pb2.PlayerParam.SerializeToString,
            service__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPlayerType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/SendPlayerType',
            service__pb2.PlayerType.SerializeToString,
            service__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInitMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/GetInitMessage',
            service__pb2.Empty.SerializeToString,
            service__pb2.InitMessageFromServer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendByeCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.Game/SendByeCommand',
            service__pb2.Empty.SerializeToString,
            service__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
