
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for index in range(415, 648):
        if is_prime(lst[index]):
            primes.append(lst[index])
    return sorted(primes)
