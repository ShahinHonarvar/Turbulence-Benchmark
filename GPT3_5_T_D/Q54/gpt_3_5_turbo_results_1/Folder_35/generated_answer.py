
from math import isqrt

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[177]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
