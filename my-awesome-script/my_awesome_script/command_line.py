"""A command-line tool for code highlighting, fancy text and local time."""
import argparse
import sys
from datetime import datetime

import pytz
from cowpy import cow
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers import get_lexer_by_name


def initialize_parser():
    """Initialize parser for CLI."""
    parser = argparse.ArgumentParser(
        usage='my-awesome-script <command> [parameter]',
    )

    subparsers = parser.add_subparsers(
        dest='command',
        title='Commands',
        metavar='<command>',
    )

    highligh = subparsers.add_parser('highligh', help='Syntax highlighting.')
    highligh.add_argument('code', help='Code to highlight.')
    cowsay = subparsers.add_parser('cowsay', help='Cow text framing.')
    cowsay.add_argument('phrase', help='Phrase to return.')
    time = subparsers.add_parser('time', help='Time in a given location.')
    time.add_argument('location', help='Location for time.')

    return parser


def my_awesome_script():
    """Parse command line input."""
    parser = initialize_parser()

    args = parser.parse_args()

    if args.command == 'highligh':
        lexer = get_lexer_by_name('python', stripall=True)
        sys.stdout.write(highlight(args.code, lexer, TerminalFormatter()))

    if args.command == 'cowsay':
        sys.stdout.write(cow.Cowacter().milk(args.phrase))
        sys.stdout.write('\n')

    if args.command == 'time':
        tz = pytz.timezone(args.location)
        sys.stdout.write(datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M:%S\n'))
