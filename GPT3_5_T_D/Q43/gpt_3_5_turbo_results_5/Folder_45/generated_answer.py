
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(23, 40):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort()
    return primes
