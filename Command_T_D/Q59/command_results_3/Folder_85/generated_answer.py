import sys
import bisect
import heapq
def all_left_truncatable_prime(n):
    sys.setrecursionlimit(1_000_000)
    n_str = str(n)
    lst = []
    for x in range(2, int(n_str[0]) + 1):
        if all(str(x + i) in n_str for i in range(1, len(n_str))):
            lst.append(x)
    return sorted(lst)
