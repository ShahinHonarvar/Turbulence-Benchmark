import sys
def find_divisors_in_range(n):
    #sys.setrecursionlimit(10**6)
    if n <= 2:
        return []
    if n <= 6:
        return [x for x in range(3, n+1) if n % x == 0]
    return []
