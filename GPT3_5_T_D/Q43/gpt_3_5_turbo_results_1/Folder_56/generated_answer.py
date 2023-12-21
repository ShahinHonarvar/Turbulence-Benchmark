
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = []
    for i in range(40, 69):
        if is_prime(nums[i]):
            primes.append(nums[i])
    primes.sort(reverse=True)
    return primes
