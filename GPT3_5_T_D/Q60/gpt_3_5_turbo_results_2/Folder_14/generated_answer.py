
from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n: int) -> bool:
    if not is_prime(n):
        return False

    digits = str(n)
    for i in range(1, len(digits)):
        if not is_prime(int(digits[i:])):
            return False
        if not is_prime(int(digits[:i])):
            return False

    return True

def all_left_right_truncatable_prime(nums: tuple) -> list:
    x = nums[78]
    result = []
    for num in range(x, 2, -1):
        if is_truncatable_prime(num):
            result.append(num)
    
    return result
