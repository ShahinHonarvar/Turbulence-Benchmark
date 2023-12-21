import sys
def find_original_set(s):
    from heapq import heapify, heappop
    hq = []
    for x in s:
        if x not in hq:
            heapify(hq)
            hq.append(x)
    hq.sort()
    x = set()
    while hq:
        s = heappop(hq)
        for i in range(len(s)):
            if s[i] not in x:
                x.add(s[i])
        if x == s:
            return x
    return x
