import socket
import sys


class Client:
    def __init__(self, target, port):
        self.target = target
        self.port = port

    def send(self, buffer):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            while True:
                client.connect((self.target, self.port))
                if not len(buffer):
                    raise Exception('Empty buffer.')

                client.send(buffer)
                recv_len = 1
                response = []

                while recv_len:
                    data = client.recv(4096)
                    recv_len = len(data)
                    response.append(data)

                print(str(response))

                del response

                buffer = sys.stdin.read()

                continue
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
