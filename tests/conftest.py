import pytest

from api.generated.greeter_pb2_grpc import add_GreeterServicer_to_server, GreeterStub
from api.core.greeter import Greeter


@pytest.fixture(scope="module")
def grpc_add_to_server():
    return add_GreeterServicer_to_server


@pytest.fixture(scope="module")
def grpc_servicer():
    return Greeter()


@pytest.fixture(scope="module")
def grpc_stub(grpc_channel):
    return GreeterStub(grpc_channel)
