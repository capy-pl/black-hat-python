from lib import parser
import sys


def main():
    args = vars(parser.parse_args())
    if args['listen'] and args['port'] > 0:
        buffer = sys.stdin.read()


if __name__ == "__main__":
    main()
