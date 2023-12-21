
from math import isqrt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[73]
    primes = []
    for i in range(10, x):
        if is_prime(i):
            num = str(i)
            truncatable = True
            for j in range(1, len(num)):
                if not is_prime(int(num[j:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
