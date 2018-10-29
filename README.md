# Canvass Analytics - Software Engineering Coding Challenges
Michael Sarfati
10-23-2018

## Run Instructions

1. You must have Python 3.5 or greater
2. Provide an exercise number (either 1 or 2 -- refer to challenge.md) and invoke the application. Eg:
    `python run.py 1`
    `./run.py 2`
3. Observe the results.

## Implementation Discussions

### Exercise 1

Code for the first exercise is housed in `./challenge/first.py`. I decided to implement this in a functional programming-like manner, with clear separation of duties to be in line with the principle of composability.

One will notice that the `fizzbuzz` step has support for dependency injection -- that is, support for hotswapping the filter function used to iterate over the data -- so that in theory, one could use a different implementation to implement exercise1.

A separate function `printableSequence` is used to render the data in the desired comma-separated form.

### Exercise 2

Due to time constraints, this is admittedly a naive implementation, relying on the simplicity of the standard library. I had experimented briefly with `pandas`, `numpy`, and `csv`, but found they were a bit too slow due to the overhead involved in these modules.

Instead, my solution works closer to the bytestream of the CSV files, parsing out each line at a time. After parsing each row, and converting the `Date` field to a Pythonic Datetime object, the solution determines which `Device_ID` the row belongs to, and appends its respective lists. At the end of the parsing-and-collecting phase, both of the lists are then sorted asynchronously (using Python's standard sort, which uses [Timsort](https://en.wikipedia.org/wiki/Timsort)) and returned, and then written out to disk.

Insertion sort is something I had considered in writing this application, however, this would have required a lot more time to write, verify, and manage Pythonic nuances in the implementation of an algorithm. Python does have such a solution contained in the `bisect` module; however, `bisect` has no support for sorting by keys in multidimensional arrays, as we are dealing with here when we want to sort each row by date. This lack of support is something that has been requested for a while in Python ( see https://bugs.python.org/issue4356 ). Other languages seem to have more native support for insertion sort (like Golang).

If I was planning on building out a much larger and more scalable solution, I would spend time doing more research on the most effective ways to tackle this. I suspect the most efficient solution that would involve writing a parser that works directly on the I/O stream of the data, and then performs insertion sort according to our criteria. This would also best be implemented in a compiled language, rather than interpreted one like Python.