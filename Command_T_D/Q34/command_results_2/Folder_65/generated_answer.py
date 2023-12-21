import sys
import heapq
def find_original_set(subsets):
    sets = set()
    for s in subsets:
        new_set = set(s)
        while not new_set & sets:
            sets.add(new_set)
            new_set = set(s)
            # heapq.heappush(sets, new_set)
        # heapq.heapify(sets)
    return sets
