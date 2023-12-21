import sys
from functools import reduce
from operator import mul
def find_subset_of_length_n(s):
    return reduce(mul, (1 for i in range(len(s)) if i+22 <= len(s)), 1)
