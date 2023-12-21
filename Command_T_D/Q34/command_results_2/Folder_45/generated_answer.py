import sys
import heapq
def find_original_set(s):
    hq = []
    for i in range(len(s)):
        hq.append([s[i], i])
    heapq.heapify(hq)
    hq.sort(key=lambda x: x[1])
    return set(hq[0][0])
