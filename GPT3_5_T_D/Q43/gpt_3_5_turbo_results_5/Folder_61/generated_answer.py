
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for num in lst[3:9]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)
