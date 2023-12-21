import sys
import functools
@functools.lru_cache(maxsize=10**6)
def find_subset_of_length_n(s):
    if len(s) == 0:
        return 1
    return sum(find_subset_of_length_n(s[:i]) for i in range(len(s)))
