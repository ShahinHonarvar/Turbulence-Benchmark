import functools
import heapq
@functools.lru_cache(maxsize=78)
def find_original_set(X):
    res = set()
    for s in X:
        m = heapq.meld(res, s)
        if m == res:
            return m
        res = m
    return res
