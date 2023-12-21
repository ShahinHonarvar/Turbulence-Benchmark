
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    temp = n
    while temp > 0:
        if not is_prime(temp):
            return False
        temp //= 10
    return True

def all_right_truncatable_prime(nums):
    x = nums[26]
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
