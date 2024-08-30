"""
demonstration of defining a sort_key method for sorting
"""

import random
import time


class MySimpleObject:
    """
    simple class to demonstrate a simple sorting key method
    """

    def __init__(self, val):
        self.val = val

    def sort_key(self):
        """
        sorting key function --used to pass in to sort functions
        to get faster sorting

        Example::

          sorted(list_of_simple_objects, key=MySimpleObject.sort_key)

        """
        return self.val

    def __lt__(self, other):
        """
        less than --required for regular sorting
        """
        return self.val < other.val

    def __repr__(self):
        return "MySimpleObject({})".format(self.val)


if __name__ == "__main__":
    N = 10000
    a_list = [MySimpleObject(random.randint(0, 10000)) for i in range(N)]
    # print("Before sorting:", a_list)

    print("Timing for {} items".format(N))
    start = time.perf_counter()
    sorted(a_list)
    reg_time = time.perf_counter() - start
    print("regular sort took: {:.4g}s".format(reg_time))

    start = time.perf_counter()
    sorted(a_list, key=MySimpleObject.sort_key)
    key_time = time.perf_counter() - start
    print("key sort took: {:.4g}s".format(key_time))

    print("performance improvement factor: {:.4f}".format((reg_time / key_time)))
