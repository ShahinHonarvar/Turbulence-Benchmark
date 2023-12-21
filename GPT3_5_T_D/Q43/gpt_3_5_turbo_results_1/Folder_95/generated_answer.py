
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(19, 72):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)
