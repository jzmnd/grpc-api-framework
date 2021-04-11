import os
import asyncio
import logging
import logging.config

import grpc
from grpc_reflection.v1alpha import reflection
import yaml

from generated import greeter_pb2_grpc, greeter_pb2
from core.greeter import Greeter
from config import SERVER_PORT

LOGGER = logging.getLogger(__name__)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def read_config(fname):
    """Read YAML config file"""
    with open(fname, "r") as f:
        config = yaml.safe_load(f)
    return config


class Server:

    """gRPC server class"""

    service_names = (
        greeter_pb2.DESCRIPTOR.services_by_name["Greeter"].full_name,
        reflection.SERVICE_NAME,
    )

    def __init__(self, port):
        """Initialize class"""
        self.port = port

    async def run(self):
        """Run the server"""
        server = grpc.aio.server()
        greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
        reflection.enable_server_reflection(self.service_names, server)

        server.add_insecure_port(self.port)
        LOGGER.info("Starting server on port %s", self.port)
        await server.start()
        await server.wait_for_termination()


if __name__ == "__main__":
    logging.config.dictConfig(read_config(os.path.join(DIR_PATH, "logging.yaml")))
    asyncio.run(Server(port=SERVER_PORT).run())
