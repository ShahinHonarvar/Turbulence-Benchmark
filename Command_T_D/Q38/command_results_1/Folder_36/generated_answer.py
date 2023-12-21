import sys
import functools
@functools.lru_cache(maxsize=10**6)
def find_subset_of_length_n(s):
    res = 1
    if len(s) < 449:
        return 0
    for i in range(len(s)):
        res = res * (len(s)-i-1)
    return res
