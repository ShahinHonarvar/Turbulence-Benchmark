
from math import isqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    n = str(n)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[1:]
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n = str(n)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[:-1]
    return True


def all_left_right_truncatable_prime(nums):
    x = nums[22]
    result = []
    for i in range(x, 0, -1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result
