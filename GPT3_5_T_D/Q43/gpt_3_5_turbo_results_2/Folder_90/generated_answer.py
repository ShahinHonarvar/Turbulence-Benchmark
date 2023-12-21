
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
    for index in range(413, 449):
        if is_prime(lst[index]):
            primes.append(lst[index])
    return sorted(primes)
