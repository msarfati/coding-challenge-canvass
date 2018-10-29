import datetime as dt
from typing import Any, Callable, Iterable, List, Type, Tuple


# A datetime format string
STRFSLASH = '%m/%d/%y'
# Another datetime format string used by our CSV
STRFDASH = '%Y-%m-%d'
# A custom-specified value to be used as NaN, useful for our sort's key comparitor
DATETIME_NAN = dt.datetime(2499, 1, 1)


def parseDate(s: str) -> dt.datetime:
    '''
    Parses a string into a Python datetime object, or DATETIME_NAN if empty or unreadable.

    :param s: A string expected to be convertable to a datetime object.
    :returns: A datetime.datetime representation of the string.
    '''

    if '/' in s:
        try:
            return dt.datetime.strptime(s, STRFSLASH)
        except ValueError:
            return DATETIME_NAN

    elif '-' in s:
        try:
            return dt.datetime.strptime(s, STRFDASH)
        except ValueError:
            return DATETIME_NAN
    else:
        return DATETIME_NAN


def convertDate(d: dt.datetime) -> str:
    '''
    Converts a datetime.datetime object to the desired format for printing ( '%m/%d/%y' ).

    :param d: A datetime.datetime object.
    :returns: String representation of datetime.datetime.
    '''

    return d.strftime(STRFSLASH) if d is not DATETIME_NAN else ''


def datetimeSortKey(item: list) -> dt.datetime:
    '''
    The function used by the built-in Python `sort` key argument, pointing to the date field.

    :param item: List of expected type.
    :returns: The datetime key to be consumed by Python `sort`
    '''

    return item[5]


def sortDatetime(*lists: list):
    '''
    Sorts a list by its datetime field.

    :param *lists: A variadic argument of any list.
    :return: Nothing, produces sideeffect of sorted list.
    '''

    for l in lists:
        l.sort(key=datetimeSortKey)


def analyzeCSV(filepath: str) -> Tuple[str, List[List[Any]]]:
    '''
    Analyzes a CSV with the criteria provided for in the challenge.

    :param filepath: A string or buffer pointing to a valid filelike object.
    :returns: The header column-names of the CSV, and all of its associated analyzed data.
    '''

    with open(filepath, 'r+') as fp:
        header = fp.readline().strip()
        dev1 = []  # type: List[List[Any]]
        dev2 = []  # type: List[List[Any]]

        for row in fp:
            item = row.split(',')

            devID = item[0]
            date = parseDate(item.pop().strip())
            item.append(date)

            if devID == '1':
                dev1.append(item)

            if devID == '2':
                dev2.append(item)

    sortDatetime(dev1, dev2)

    return header, dev1 + dev2


def writeCSV(filepath: str, header: List[Any], lst: List[List[Any]]):
    '''
    Creates a new CSV on disk, conforming to requirements of the challenge.

    :param filepath: Valid path to a file on system.
    :param header: A comma-separated string of column names.
    :param lst: A two-dimensional list.
    '''

    with open(filepath, 'w+') as fp:
        fp.write('{0}{1}'.format(header, '\n'))
        for item in lst:
            item[5] = convertDate(item[5])
            fp.write(','.join(item) + '\n')
