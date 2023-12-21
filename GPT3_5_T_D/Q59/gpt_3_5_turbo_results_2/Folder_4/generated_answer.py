
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[96]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            is_left_truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
