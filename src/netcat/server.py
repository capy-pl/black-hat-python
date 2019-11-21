from ipaddress import ip_address
import socket
from threading import Thread
import subprocess
from typing import Dict


class Server:
    def __init__(self, target: str = '0.0.0.0', port: int = 3000):
        self.target = str(ip_address(target))
        self.port = port

    def listen(self, args: Dict):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.target, self.port))
        server.listen(5)
        print('Server is listening on {}:{}'.format(self.target, self.port))

        while True:
            try:
                client_socket, _ = server.accept()
                client_thread = Thread(target=handler, args=(client_socket,), kwargs={
                    'upload_destination': args['upload'],
                    'interactive': args['interactive'],
                    'execute': args['execute']
                })
                client_thread.start()

            except socket.timeout:
                server.close()
                exit(0)

            except KeyboardInterrupt:
                server.close()
                print('Keyboad interrupt. Program exit.')
                exit(0)

            except:
                print('Something happened.')
                server.close()
                exit(0)


def handler(client_socket: socket.socket, upload_destination: str = '', interactive: bool = False, execute: str = ''):
    if upload_destination is not None and len(upload_destination):
        upload_destination = upload_destination.lstrip().rstrip()
        file_buffer = b''
        while True:
            data = client_socket.recv(1024)
            if len(data) > 0:
                file_buffer += data
            else:
                break
        try:
            with open(upload_destination, 'wb') as file:
                file.write(file_buffer)
            client_socket.send('Successfully saved file to {}.'.format(
                upload_destination).encode('utf8'))
        except:
            client_socket.send('Failed to save file to {}. Please try again.'.format(
                upload_destination).encode('utf8'))

    if execute is not None and len(execute):
        output = run_command(execute)
        client_socket.send(output.encode('utf8'))

    if interactive:
        while True:
            client_socket.send(b'<BHP:#> ')
            cmd_buffer = b''

            while b'\n' not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            cmd = str(cmd_buffer)
            cmd = cmd.split('\n')[0]
            output = run_command(cmd)

            client_socket.send(output.encode('utf8'))


def run_command(command: str) -> str:
    command = command.rstrip()
    command = command.split()

    try:
        completed_process = subprocess.run(
            command, capture_output=True, encoding='utf8')
        return completed_process.stdout
    except subprocess.CalledProcessError:
        print('Command execute failed.')
        return completed_process.stderr
