import sys
import functools
@functools.lru_cache(maxsize=10**6)
def find_original_set(set1, set2):
    return set1 | set2
