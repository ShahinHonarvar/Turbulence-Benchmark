
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
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            left_num = num
            right_num = num
            while len(str(left_num)) > 2:
                left_num //= 10
                if not is_prime(left_num):
                    truncatable = False
                    break
            while len(str(right_num)) > 2:
                right_num %= 10 ** (len(str(right_num)) - 1)
                if not is_prime(right_num):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)
