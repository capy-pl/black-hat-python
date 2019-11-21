import sys
from typing import Dict


from .server import Server
from .client import Client


def netcat(args: Dict):
    if not args['listen']:
        client = Client(args['target'], args['port'])
        client.connect()
    else:
        server = Server(args['target'], args['port'])
        server.listen(args)
