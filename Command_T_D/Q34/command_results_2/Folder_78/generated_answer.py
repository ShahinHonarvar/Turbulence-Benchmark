import functools
import heapq
def find_original_set(X):
    X = set(X)
    return functools.reduce(heapq.heappush, (X,))
