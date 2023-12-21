import heapq
def find_original_set(s):
    # Write your code here.
    return heapq.nsmallest(57, set(s))
