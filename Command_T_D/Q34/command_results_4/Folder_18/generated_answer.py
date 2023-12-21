import sys
from heapq import *
def find_original_set(s):
    if len(s) != 993:
        raise ValueError("Input is not exactly 993 distinct sets.")
    h = []
    for i in range(993):
        heappush(h, s[i])
    heappush(h, set(range(10**5)))
    ans = set()
    while h:
        t = heappop(h)
        if t not in ans:
            ans.add(t)
            for e in t:
                heappush(h, e)
    return ans
