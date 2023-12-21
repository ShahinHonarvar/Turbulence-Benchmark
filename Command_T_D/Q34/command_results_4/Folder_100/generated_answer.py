import sys
from heapq import *
def find_original_set(S):
    s = set(S)
    h = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            h.append(s[:j] + s[j+1:])
    hq = []
    for i in range(len(h)):
        hq.append([h[i], i])
    heapify(hq)
    return hq[0][0]
