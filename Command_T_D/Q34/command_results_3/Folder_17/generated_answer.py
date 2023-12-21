from functools import reduce
from heapq import *
def find_original_set(sets):
    return reduce(set.union, sets)
