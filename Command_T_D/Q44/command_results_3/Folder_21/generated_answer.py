import operator as o
import functools
import sys
import collections
import heapq
import bisect
@functools.lru_cache(maxsize=10**5)
def composite_nums_between_indices(a):
    return set(a[262:746])
