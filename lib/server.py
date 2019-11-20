from ipaddress import ip_address
import socket
from threading import Thread


def handler():
    pass


class Server:
    def __init__(self, target='0.0.0.0', port):
        self.target = str(ip_address(target))
        self.port = port

    def listen():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.target, self.port))
        server.listen(5)

        while True:
            client_socket, addr = server.accept()
            client_thread = Thread(target=handler, args=(client_socket))
