
import sys
import bisect
import heapq

sys.setrecursionlimit(10**6)

def all_left_right_truncatable_prime(tup):
    start, end = map(str, (tup[86], tup[0]))
    s = set(str(p) for p in range(2, end) if all(int(d) for d in str(p) if d!="0"))
    x = list(s)
    heapq.heapify(x)
    heapq.heapify(x)
    i = len(x)-2
    while i>=0:
        p = int(x[i])
        if p>=start:
            break
        q = p
        while q:
            q //= 10
            i -= 1
        if p!=q:
            break
        i -= 1
    else:
        return []
    i = j = len(x)-1
    while j>=0:
        p = int(x[j])
        if p>=end:
            break
        q = p
        while q:
            q //= 10
            j -= 1
        if p!=q:
            break
        j -= 1
        if i!=j:
            break
        i -= 1
    return sorted(set(x))
