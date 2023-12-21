import sys
from heapq import *
def find_original_set(A):
    hq = []
    A = set(A)
    for x in A:
        heappush(hq, x)
    hq = sorted(hq)
    return set(hq)
