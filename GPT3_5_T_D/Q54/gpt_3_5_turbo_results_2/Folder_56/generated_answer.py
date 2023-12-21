
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[30]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            is_right_truncatable = True
            for j in range(len(num) - 1):
                num = num[:-1]
                if not is_prime(int(num)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
