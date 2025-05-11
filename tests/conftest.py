import grpc
import pytest

from greeter.v1 import greeter_pb2_grpc as greeter_v1_pb2_grpc
from api.core.greeter import Greeter


@pytest.fixture
async def grpc_server():
    server = grpc.aio.server()
    greeter_v1_pb2_grpc.add_GreeterServiceServicer_to_server(Greeter(), server)
    port = server.add_insecure_port("[::]:0")
    await server.start()
    yield f"localhost:{port}"
    await server.stop(0)


@pytest.fixture
async def grpc_greeter_service_stub(grpc_server):
    async with grpc.aio.insecure_channel(grpc_server) as channel:
        await channel.channel_ready()
        yield greeter_v1_pb2_grpc.GreeterServiceStub(channel)
