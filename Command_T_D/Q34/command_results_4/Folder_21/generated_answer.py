import heapq
def find_original_set(S):
    s = set(S)
    heapq.heapify(s)
    return heapq.nsmallest(851, s)
