
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(229, 851):
        if is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
