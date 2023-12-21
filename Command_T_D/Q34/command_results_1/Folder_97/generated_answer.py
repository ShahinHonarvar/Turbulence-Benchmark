import sys
from heapq import *
def find_original_set(s):
    if len(s) == 1:
        return s
    s = list(set(s))
    heapq.heapify(s)
    while len(s) > 1:
        v = heappop(s)
        if v:
            heappush(s, v)
            for i in range(1, len(v)):
                if v[i] not in s:
                    heappush(s, v[i])
        else:
            break
    return s
