import heapq
def find_original_set(S):
    return set(heapq.nsmallest(851, [s for s in S if s]))
