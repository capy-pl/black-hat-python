import argparse


def config_netcat_parser(parser: argparse.ArgumentParser):
    parser.add_argument('-t', '--target', required=True,
                        type=str, help='Target host address.', metavar='address')
    parser.add_argument('-p', '--port', required=True, type=int,
                        help='Target host port number.', metavar='number')
    parser.add_argument('-l', '--listen', action='store_true',
                        help='Listen on connection.')
    parser.add_argument('-e', '--execute', nargs=1,
                        metavar='command', type=str, help='Execute the command.')
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Activate interactive shell.')
    parser.add_argument('-u', '--upload', nargs=1, metavar='dest',
                        help='Upload the file upon connection open.')
