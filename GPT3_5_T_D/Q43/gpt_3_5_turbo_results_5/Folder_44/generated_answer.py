
from math import sqrt

def check_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(19, 86):
        if check_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort(reverse=True)
    return primes
