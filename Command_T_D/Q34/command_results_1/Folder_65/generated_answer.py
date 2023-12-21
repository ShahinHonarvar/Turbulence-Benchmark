import sys
import heapq
def find_original_set(s):
    m = set()
    for x in s:
        h = heapq.nsmallest(len(x), (x))
        m.update(h)
    return m
