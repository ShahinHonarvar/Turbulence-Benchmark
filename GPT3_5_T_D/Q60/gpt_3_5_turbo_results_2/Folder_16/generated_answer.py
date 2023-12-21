
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[792]
    if x < 10:
        return []
    results = []
    primes = [2, 3, 5, 7]
    while len(primes) > 0:
        prime = primes.pop(0)
        if prime <= x:
            results.append(prime)
            for d in [1, 3, 7, 9]:
                new_prime = prime * 10 + d
                if is_prime(new_prime):
                    primes.append(new_prime)
    return results
