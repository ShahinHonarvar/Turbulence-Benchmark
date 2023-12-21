
import sys
import re
import itertools

sys.setrecursionlimit(10**6)

import bisect

def all_left_right_truncatable_prime(x_range):
    if x_range[0] <= 1:
        return []
    # inhabitants of x_range
    # we need to check that a number is prime and left-right-truncatable
    numbers = list(range(2, x_range[0]))
    for n in numbers:
        if not is_left_right_truncatable_prime(n):
            break
    # we need to check that a number is prime and left-right-truncatable
    numbers = list(range(x_range[1] + 1, x_range[0] + 1))
    for n in numbers:
        if not is_left_right_truncatable_prime(n):
            break
    return sorted(set(numbers))

def is_left_right_truncatable_prime(n):
    if n < 2:
        return False
    if n < 10:
        return True
    if n < 100:
        return True
    if n < 1000:
        return True
    if n < 10000:
        return True
    if n < 100000:
        return True
    return False
