# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import users_pb2 as users__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in users_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UserExist = channel.unary_unary(
                '/Users/UserExist',
                request_serializer=users__pb2.UserRequest.SerializeToString,
                response_deserializer=users__pb2.ExistResponse.FromString,
                _registered_method=True)
        self.UserMarks = channel.unary_unary(
                '/Users/UserMarks',
                request_serializer=users__pb2.UserRequest.SerializeToString,
                response_deserializer=users__pb2.MarksResponse.FromString,
                _registered_method=True)
        self.FilmRating = channel.unary_unary(
                '/Users/FilmRating',
                request_serializer=users__pb2.RatingRequest.SerializeToString,
                response_deserializer=users__pb2.RatingResponse.FromString,
                _registered_method=True)
        self.UserMarksUpdate = channel.unary_unary(
                '/Users/UserMarksUpdate',
                request_serializer=users__pb2.MarksUpdateRequest.SerializeToString,
                response_deserializer=users__pb2.Nill.FromString,
                _registered_method=True)


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UserExist(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserMarks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FilmRating(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserMarksUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UserExist': grpc.unary_unary_rpc_method_handler(
                    servicer.UserExist,
                    request_deserializer=users__pb2.UserRequest.FromString,
                    response_serializer=users__pb2.ExistResponse.SerializeToString,
            ),
            'UserMarks': grpc.unary_unary_rpc_method_handler(
                    servicer.UserMarks,
                    request_deserializer=users__pb2.UserRequest.FromString,
                    response_serializer=users__pb2.MarksResponse.SerializeToString,
            ),
            'FilmRating': grpc.unary_unary_rpc_method_handler(
                    servicer.FilmRating,
                    request_deserializer=users__pb2.RatingRequest.FromString,
                    response_serializer=users__pb2.RatingResponse.SerializeToString,
            ),
            'UserMarksUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.UserMarksUpdate,
                    request_deserializer=users__pb2.MarksUpdateRequest.FromString,
                    response_serializer=users__pb2.Nill.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Users', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UserExist(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Users/UserExist',
            users__pb2.UserRequest.SerializeToString,
            users__pb2.ExistResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UserMarks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Users/UserMarks',
            users__pb2.UserRequest.SerializeToString,
            users__pb2.MarksResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def FilmRating(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Users/FilmRating',
            users__pb2.RatingRequest.SerializeToString,
            users__pb2.RatingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UserMarksUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Users/UserMarksUpdate',
            users__pb2.MarksUpdateRequest.SerializeToString,
            users__pb2.Nill.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
