import pytest

from greeter.v1.greeter_pb2_grpc import add_GreeterServiceServicer_to_server, GreeterServiceStub
from api.core.greeter import Greeter


@pytest.fixture(scope="module")
def grpc_add_to_server():
    return add_GreeterServiceServicer_to_server


@pytest.fixture(scope="module")
def grpc_servicer():
    return Greeter()


@pytest.fixture(scope="module")
def grpc_stub(grpc_channel):
    return GreeterServiceStub(grpc_channel)
