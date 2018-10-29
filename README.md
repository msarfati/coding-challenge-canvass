# Canvass Analytics - Software Engineering Coding Challenges
Michael Sarfati

## Run Instructions

1. You must have Python version 3.7 and pip installed
2. Create a virtual environment for the application and activate it.
   1. `python3 -m venv .`
   2. `source bin/activate`
3. Install dependencies
    1. `pip install -r requirements.txt`
4. Provide an exercise number (either 1 or 2 -- refer to challenge.md) and invoke the application. Eg:
    `python run.py 1`
    `./run.py 2`
5. Observe the results!

## Implementation Discussions

### Exercise 1

Code for the first exercise is housed in `./challenge/first.py`. I decided to implement this in a functional programming-like manner, with clear separation of duties to be in line with the principle of composability.

One will notice that the `fizzbuzz` step has support for dependency injection -- that is, support for hotswapping the filter function used to iterate over the data -- so that in theory, one could use a different implementation to implement exercise1.

A separate function `printableSequence` is used to render the data in the desired comma-separated form.

### Exercise 2
