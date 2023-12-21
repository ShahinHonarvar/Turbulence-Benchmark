import sys
import functools
@functools.lru_cache(maxsize=10**6)
def find_subset_of_length_n(s):
    if len(s) < 88:
        return 0
    return sum(find_subset_of_length_n(x) for x in s)
