import sys
from functools import reduce
from operator import xor
def find_original_set(*other_sets):
    result = reduce(xor, (ORIGINAL_SET, *other_sets))
    return result
