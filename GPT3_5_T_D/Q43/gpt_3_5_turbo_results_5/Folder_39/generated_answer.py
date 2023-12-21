
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

def find_primes_between_indices(numbers):
    primes = []
    for index in range(69, 81):
        if is_prime(numbers[index]):
            primes.append(numbers[index])
    primes.sort()
    return primes
