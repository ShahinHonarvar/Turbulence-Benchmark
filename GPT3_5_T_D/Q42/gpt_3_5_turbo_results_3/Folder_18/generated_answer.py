
from math import sqrt

def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    number = lst[312]
    factors = set()
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            factors.add(i)

    return factors
