import sys
import heapq
def find_original_set(s):
    s = sorted(s)
    q = set(s)
    h = [(q, len(q))]
    heapq.heapify(h)
    while h:
        q, sz = heapq.heappop(h)
        if sz == len(s):
            return q
        new = set()
        for i in range(sz):
            new.update(q[i])
        heapq.heappush(h, (new, sz + 1))
    return q
