import sys
from functools import reduce
from heapq import heappush, heappop
def find_original_set(s):
    return reduce(set.intersection, s)
