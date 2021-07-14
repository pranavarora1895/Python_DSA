"""Learn to make the command line utility in python which can be used in other applications"""

import argparse
import sys


def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return 'Something went wrong'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Add 1st float value")
    parser.add_argument('--y', type=float, default=2.0, help="Add 2nd float value")
    parser.add_argument('--o', type=str, default="add", help="choose among add sub mul div")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

# python_utility.py --x 8 --y 9 --o mul
