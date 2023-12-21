
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = []
    for num in nums[1:3]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)
