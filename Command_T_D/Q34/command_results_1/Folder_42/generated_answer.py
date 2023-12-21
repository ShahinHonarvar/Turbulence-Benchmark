from functools import reduce
from operator import and_
from heapq import *
def find_original_set(s):
    if len(s) == 0:
        return set()
    s = set(s)
    s = [s]
    for i in range(1, 849):
        s += [[s]]
    s = reduce(and_, s)
    return s
