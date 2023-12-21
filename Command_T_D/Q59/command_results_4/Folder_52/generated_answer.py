import sys
def all_left_truncatable_prime(n):
    sys.setrecursionlimit(10**6)
    return [str(p) for p in range(2, n[0] + 1) if all(int(d) for d in str(p) if d!="0" and str(p)[0] != d)]
