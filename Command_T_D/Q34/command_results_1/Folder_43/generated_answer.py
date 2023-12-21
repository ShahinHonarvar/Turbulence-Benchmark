import sys
import heapq
def find_original_set(s):
    # Create a heap of sets
    heapq.heapify(s)
    # Remove all sets
    while s:
        s.pop()
        # Union all sets
        s = set.union(s)
    return s
