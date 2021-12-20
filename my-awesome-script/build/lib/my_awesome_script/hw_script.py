"""This script read command and text from terminal and return the answer."""
import argparse
import datetime
import sys

import pytz
from cowpy import cow
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer


def highligh(text):
    """
    Wrap the text.

    :return: None
    """
    sys.stdout.write(highlight(text, PythonLexer(), TerminalFormatter()))
    sys.stdout.write('\n')


def cowsay(text):
    """
    Wrap the text.

    :return: None
    """
    # Create a Cow with a thought bubble, a tongue
    cheese = cow.Moose(thoughts=True, tongue=True)

    # Get a cowsay message by milking the cow
    msg = cheese.milk(text)
    sys.stdout.write(msg)
    sys.stdout.write('\n')


def time(location):
    """
    Wrap the location.

    :return: None
    """
    location_timezone = pytz.timezone(location)
    location_time = datetime.datetime.now(location_timezone)
    sys.stdout.write(location_time.strftime('%H:%H:%S'))
    sys.stdout.write('\n')


def main():
    """
    Do the script.

    :return: None
    """
    str1 = 'Use commands: higligh, cowsay, time'
    str2 = 'Write: what to highlight, what has cow say, time you want to know'
    parser = argparse.ArgumentParser()
    parser.add_argument('com', type=str, default='', help=str1)
    parser.add_argument('text', type=str, default='', help=str2)
    args = parser.parse_args()
    if args.com == 'highligh':
        highligh(args.text)
    elif args.com == 'cowsay':
        cowsay(args.text)
    elif args.com == 'time':
        time(args.text)
