import logging

from grpc_interceptor.exceptions import InvalidArgument

from generated import greeter_pb2, greeter_pb2_grpc

LOGGER = logging.getLogger(__name__)


class Greeter(greeter_pb2_grpc.GreeterServicer):

    """Greeter class"""

    title_map = {
        greeter_pb2.GreeterRequest.Title.NONE: "",
        greeter_pb2.GreeterRequest.Title.LORD: "Lord ",
        greeter_pb2.GreeterRequest.Title.MONARCH: "Your Highness ",
    }

    async def Reply(self, request, context):
        """Provides a greeting."""
        if request.age < 0:
            raise InvalidArgument("Invalid age argument. Must be >= 0.")

        greeting = "Hello {title}{name}! You are {age} years old.".format(
            title=self.title_map[request.title],
            name=request.name,
            age=request.age,
        )
        LOGGER.info("Sending a reply to %s", request.name)
        return greeter_pb2.GreeterReply(greeting=greeting)
