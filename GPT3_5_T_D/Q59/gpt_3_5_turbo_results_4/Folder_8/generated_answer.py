
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

def all_left_truncatable_prime(nums):
    x = nums[41]
    result = []
    for i in range(x-1, 0, -1):
        if '0' not in str(i):
            is_truncatable_prime = True
            truncated_num = str(i)
            while len(truncated_num) > 1:
                truncated_num = truncated_num[1:]
                if not is_prime(int(truncated_num)):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(i)
    return result
