#!/usr/bin/env python

"""
hand writing 'for'

demonstrates how for interacts with an iterable
"""


x = [1, 2, 3, 4, 5,]


def my_for(an_iterable, func):
    """
    Emulation of a for loop.

    func() will be called with each item in an_iterable

    :param an_iterable: anything that satisfies the iteration protocol

    :param func: a callable -- it will be called, passing in each item
                 in an_iterable.

    """
    # equiv of "for i in x:"
    iterator = iter(an_iterable)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        func(i)


if __name__ == "__main__":

    def print_func(x):
        print(x)

    x = [1, 2, 3, 4, 5,]
    my_for(x, print_func)

    t = ('a', 'b', 'c', 'd')

    my_for(t, print_func)
