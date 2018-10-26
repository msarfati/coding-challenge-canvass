#!/usr/bin/env python

import argparse
from challenge import first

def challenge1():
    '''
    Performs necessary setup procedures for generating required challenge.
    '''
    dataSet = range(1000, 3001)
    fizzbuzzed = first.process(dataSet, first.allEven)
    printFizzbuzz = first.printableSequence(fizzbuzzed)
    print(printFizzbuzz)


def challenge2():
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'challenge',
        help='The challenge number you wish to invoke (accepted: 1, 2)',
        type=int,
    )
    args = parser.parse_args()
    if args.challenge == 1:
        challenge1()
    elif args.challenge == 2:
        challenge2()
    else:
        print("Unknown option.")

if __name__ == '__main__':
    main()
