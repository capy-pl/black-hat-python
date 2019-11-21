import argparse

from .netcat import config_netcat_parser

parser = argparse.ArgumentParser(description='Blackhat python example.')

subparsers = parser.add_subparsers(dest='command')

config_netcat_parser(subparsers.add_parser('netcat'))
