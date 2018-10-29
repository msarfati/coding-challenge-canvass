import math
from typing import Callable, Iterable, List, Type


def allEven(num: int) -> bool:
    '''
    Evaluates whether every digit in a number is even.

    This function iterates over each digit of an integer, starting from the largest digit, moving to smallest.
    Only after all digits are evaluated as even (i.e., it's modulo 2 is not equal to zero), this function will
    return True, and False in all other cases.

    :param num: num is an integer
    :returns: True if the integer is even, else False.
    '''
    digitCount = math.floor(math.log10(num)) + 1  # Derived from https://brilliant.org/wiki/finding-digits-of-a-number
    for n in range(digitCount - 1, -1, -1):  # We begin from the largest number to discard the most common the quickest
        digit = math.floor(num / 10**n)  # Retrieves the first n-th digits
        if digit % 2 != 0:  # Checks if the digit is even
            return False
    return True


def fizzbuzz(data: Iterable[int], func: Callable[[int], bool]) -> Iterable[int]:
    '''
    Processes some list based on some criteria (ie, only return a number of all of its digits are even).

    :param data: Some iterable containing only integers.
    :param func: A function that will be used filter the values of the iterable.
    :returns: An new iterable that has been processed.
    '''
    return filter(func, data)


def printableSequence(data: Iterable[int]) -> str:
    '''
    Produces a comma-separated printable sequence string of some iterable.

    :param data: Some iterable containing only integers.
    :returns: Comma-separated string of values from iterable.
    '''
    return ",".join([str(i) for i in data])  # Iterates over each element in `data` and joins it with a comma
