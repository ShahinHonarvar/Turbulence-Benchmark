import sys
from functools import reduce
from operator import mul
from math import factorial
def find_subset_of_length_n(s):
    return reduce(mul, (factorial(i) for i in range(1, len(s) + 1)))
