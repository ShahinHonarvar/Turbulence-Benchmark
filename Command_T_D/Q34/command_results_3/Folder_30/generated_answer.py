import sys
import heapq
def find_original_set(S):
    # Create a list of sets
    sets = [set(x) for x in S]
    # Create a heap from the sets
    heap = []
    for x in sets:
        heapq.heappush(heap, x)
    # Pop sets until we have the original set
    original_set = set()
    while heap:
        set_ = heapq.heappop(heap)
        if set_.issubset(original_set):
            break
        original_set.update(set_)
    # Return the original set
    return original_set
