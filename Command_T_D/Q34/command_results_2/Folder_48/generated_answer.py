import heapq as hq
def find_original_set(s):
    return set(hq.nsmallest(990, s))
