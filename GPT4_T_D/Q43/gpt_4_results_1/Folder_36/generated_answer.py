
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(integer_list):
    primes = [num for num in integer_list[229:851] if is_prime(num)]
    return sorted(primes, reverse = True)
