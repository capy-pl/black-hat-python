import sys
from typing import Dict


from .server import Server
from .client import Client


def netcat(args: Dict):
    if not args['listen']:
        data = input()
        client = Client(args['target'], args['port'])
        client.send(data.encode('utf8'))
    else:
        server = Server(args['target'], args['port'])
        server.listen(args)
