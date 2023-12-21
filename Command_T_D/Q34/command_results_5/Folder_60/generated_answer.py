import heapq as hq
def find_original_set(s):
    h = hq.nsmallest(len(s), s)
    return h
