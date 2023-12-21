
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(24, 84):
        if is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes)
