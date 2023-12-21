
import sys
import math

def all_left_right_truncatable_prime(n):
    sys.setrecursionlimit(1_000_000)
    if not (n[6] > 1):
        return []
    l = []
    for i in range(2, n[6]):
        if is_left_right_truncatable_prime(i):
            l.append(i)
    return l

def is_left_right_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1 or n == 5:
        return False
    if n < 10:
        return True
    if n < 100:
        return False
    if n < 1_000:
        return True
    if n < 10_000:
        return False
    if n < 100_000:
        return True
    if n < 1_000_000:
        return False
    return True
