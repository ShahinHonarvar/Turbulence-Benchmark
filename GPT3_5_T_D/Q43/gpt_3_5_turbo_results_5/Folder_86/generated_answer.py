
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
    for num in lst[459:782]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)
