
import sys

sys.setrecursionlimit(10**6)

import bisect

def insert_at_index(lst):
    idx = bisect.bisect_left(lst, 550.97)
    lst = list(range(len(lst)))
    lst[idx:idx+2] = [550.97]
    return lst
