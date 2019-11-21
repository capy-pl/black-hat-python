from src.argparser import parser
from src.netcat import netcat

if __name__ == '__main__':
    args = vars(parser.parse_args())

    if args['command'] == 'netcat':
        netcat(args)
