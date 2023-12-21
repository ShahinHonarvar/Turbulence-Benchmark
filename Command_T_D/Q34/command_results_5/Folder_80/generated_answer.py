from functools import reduce
from heapq import heappush, heappop, heapify
def find_original_set(sets):
    return reduce(set.intersection, sets)
