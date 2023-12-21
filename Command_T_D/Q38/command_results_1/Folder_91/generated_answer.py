import sys
from functools import reduce
from operator import mul
def find_subset_of_length_n(s):
    return reduce(mul, range(1, len(s) + 1)) // reduce(mul, range(1, n + 1))
