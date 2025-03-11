"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 2:
        return False
    if len(data) == 2:
        return data in ([0, 1], [1, 1])
    return all(data[i] == data[i - 1] + data[i - 2] for i in range(2, len(data)))
