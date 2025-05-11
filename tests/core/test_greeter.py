import grpc
import pytest

from greeter.v1 import greeter_pb2 as greeter_v1_pb2


@pytest.mark.asyncio
async def test_greeter_reply(grpc_greeter_service_stub):
    """Test greeter reply, happy path."""
    request = greeter_v1_pb2.ReplyRequest()
    request.name = "Alex"
    request.age = 10
    request.title = "TITLE_MONARCH"

    response = await grpc_greeter_service_stub.Reply(request)

    assert response.greeting == "Hello Your Highness Alex! You are 10 years old."


@pytest.mark.asyncio
async def test_greeter_reply__age_error(grpc_greeter_service_stub):
    """Test greeter reply with invalid age."""
    request = greeter_v1_pb2.ReplyRequest()
    request.name = "Alex"
    request.age = -10

    with pytest.raises(grpc.aio.AioRpcError):
        await grpc_greeter_service_stub.Reply(request)
