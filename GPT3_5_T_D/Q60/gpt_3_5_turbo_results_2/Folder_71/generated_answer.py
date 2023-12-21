
from math import isqrt

def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:i])) or not is_prime(int(str_n[i:])):
                return False
        return True

    x = nums[22]
    result = sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)
    return result
