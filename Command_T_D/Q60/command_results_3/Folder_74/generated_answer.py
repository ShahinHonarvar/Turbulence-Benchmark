
import sys
import bisect
from functools import reduce
from collections import Counter

sys.setrecursionlimit(10**6)

# This is the value of sys.maxsize - 1.
MAX_INT = sys.maxsize - 1


def prime(n):
    """
    Determine whether a number is prime or not.
    """
    if n <= 1:
        return True
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = n**0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if n % d == 0:
            return False
        d += i
        i = 6 - i
    return True


def all_left_right_truncatable_prime(test_list):
    res = []
    left_list = []
    right_list = []
    for item in test_list:
        if prime(item):
            left_list.append(item)
            right_list.append(item)
    for left in left_list:
        if left <= 9:
            break
        for right in right_list:
            if right <= 9:
                break
            if prime(left + right):
                res.append(left + right)
    return res
