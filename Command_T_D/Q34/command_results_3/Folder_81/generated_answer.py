import sys
import heapq
def find_original_set(arg):
    if len(arg) == 1:
        return list(range(len(arg[0])))
    sys.setrecursionlimit(1_000_000)
    sets = sorted(list(set(arg)), key=lambda x: len(x))
    sets = heapq.nlargest(72, sets)
    return sets
