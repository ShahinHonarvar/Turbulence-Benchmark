
from itertools import permutations
from math import sqrt

def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n%i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    x = numbers[69]
    primes = []
    for n in range(2, x):
        if is_left_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)
