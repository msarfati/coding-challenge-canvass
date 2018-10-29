#!/usr/bin/env python

import argparse
from challenge import first, second
import sys


DESCRIPTION = 'This application can be used to run the solutions to the challenge exercises.'
EPILOG = 'example: ./run.py 1'
HELP = 'The challenge number you wish to invoke (accepted: 1, 2)'

def challenge1():
    '''
    Performs necessary setup procedures for generating required challenge.
    '''
    dataSet = range(1000, 3001)
    fizzbuzzed = first.fizzbuzz(dataSet, first.allEven)
    printFizzbuzz = first.printableSequence(fizzbuzzed)
    print(printFizzbuzz)


def challenge2():
    '''
    Performs necessary setup procedures for generating required challenge.
    '''
    filepath = './data/random_data.csv'
    outputFile = './random_data_sorted.csv'

    head, data = second.analyzeCSV(filepath)
    second.writeCSV(outputFile, head, data)

    print('File created: ' + outputFile)


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
    parser.add_argument('challenge', help=HELP, type=int)
    if len(sys.argv) != 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    if args.challenge == 1:
        challenge1()
    elif args.challenge == 2:
        challenge2()
    else:
        print("Unknown option.")


if __name__ == '__main__':
    main()
