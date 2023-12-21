
import sys

def all_left_right_truncatable_prime(lim):
    #sys.setrecursionlimit(lim)
    if lim[0] <= 2:
        return []
    x = lim[0]
    res = []
    for i in range(2, int(x**(0.5)) + 1):
        for j in range(2, min(x-i, 10) + 1):
            if is_prime(x-i-j):
                res += [x-i-j]
    return res

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    maxDivisor = int(n**(0.5)) + 1
    for i in range(5, maxDivisor+1):
        if n % i == 0:
            return False
    return True
