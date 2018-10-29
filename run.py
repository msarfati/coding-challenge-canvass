#!/usr/bin/env python

import argparse
import asyncio
from challenge import first, second
import sys


DESCRIPTION = 'This application can be used to run the solutions to the challenge exercises. \
Note that \'challenge 3\' refers to running the second challenge with the large dataset.'
EPILOG = 'examples: ./run.py 1 or ./run.py 2 or ./run.py 3 '
HELP = 'The challenge number you wish to invoke (accepted: 1, 2, 3)'

CSV_FILEPATH = './data/random_data.csv'
BIG_CSV_FILEPATH = './data/large_data.csv'
OUTPUT_FILEPATH = './random_data_sorted.csv'

def challenge1():
    '''
    Performs necessary setup procedures for generating required challenge.
    '''

    dataSet = range(1000, 3001)
    fizzbuzzed = first.fizzbuzz(dataSet, first.allEven)
    printFizzbuzz = first.printableSequence(fizzbuzzed)
    print(printFizzbuzz)


def challenge2(filepath: str):
    '''
    Performs necessary setup procedures for generating required challenge.

    :param filepath: A string or buffer pointing to a valid filelike object.
    '''

    print('Processing: ' + filepath)

    head, data = second.analyzeCSVRunner(filepath)
    second.writeCSV(OUTPUT_FILEPATH, head, data)

    print('File created: ' + OUTPUT_FILEPATH)


def main():
    '''
    Main execution thread.
    '''

    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
    parser.add_argument('challenge', help=HELP, type=int)
    if len(sys.argv) != 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    if args.challenge == 1:
        challenge1()
    elif args.challenge == 2:
        challenge2(CSV_FILEPATH)
    elif args.challenge == 3:
        challenge2(BIG_CSV_FILEPATH)
    else:
        print("Unknown option.")


if __name__ == '__main__':
    main()
