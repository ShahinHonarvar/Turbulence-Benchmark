
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[87]
    result = []
    for n in range(2, x + 1):
        if is_prime(n):
            str_n = str(n)
            if '0' not in str_n:
                truncatable = True
                for i in range(1, len(str_n)):
                    left_truncated = int(str_n[i:])
                    right_truncated = int(str_n[:-i])
                    if not is_prime(left_truncated) or not is_prime(right_truncated):
                        truncatable = False
                        break
                if truncatable:
                    result.append(n)
    return result
