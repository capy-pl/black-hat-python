import socket
import sys
from ipaddress import ip_address


class Client:
    def __init__(self, target: str, port: int):
        self.target = str(ip_address(target))
        self.port = port

    def connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((self.target, self.port))
            while True:
                recv_len = 1
                response = b''
                while recv_len:
                    data = client.recv(4096)
                    recv_len = len(data)
                    response += data
                    
                    # no more data
                    if recv_len < 4096:
                        break

                print(response.decode(), end='')

                del response

                buffer = input().encode('utf8')
                buffer += b'\n'

                client.send(buffer)

        except KeyboardInterrupt:
            print('KeyboardInterrupt detected.')
            print('Close connection.')
            client.close()
            print('Program exit.')
            exit(0)

        except Exception as err:
            print('Exception: {}'.format(err))
            print('Close connection.')
            client.close()
            print('Program exit.')
            exit(1)
