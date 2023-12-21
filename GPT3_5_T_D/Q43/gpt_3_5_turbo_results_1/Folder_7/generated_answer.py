
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[239:687]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)
