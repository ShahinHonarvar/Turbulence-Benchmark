import sys
import functools
import operator
@functools.lru_cache(maxsize=1_000_000)
def find_subset_of_length_n(n):
    return 2**n.bit_length()
