import sys
import functools
@functools.lru_cache(maxsize=10**5)
def find_original_set(X):
    if X:
        return find_original_set(X.union(X))
    return set()
