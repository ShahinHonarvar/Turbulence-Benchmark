import heapq
def find_original_set(s):
    return set(heapq.nsmallest(63, list(range(len(s)))))
