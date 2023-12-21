
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(59, 97+1):
        if is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
