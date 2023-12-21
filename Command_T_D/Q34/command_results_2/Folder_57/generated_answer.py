from functools import reduce
from operator import xor
def find_original_set(A):
    return reduce(xor, map(set, A))
