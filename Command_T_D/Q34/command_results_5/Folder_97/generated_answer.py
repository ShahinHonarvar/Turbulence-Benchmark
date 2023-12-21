from functools import reduce
from operator import xor
def find_original_set(s):
    return reduce(xor, map(set, s))
