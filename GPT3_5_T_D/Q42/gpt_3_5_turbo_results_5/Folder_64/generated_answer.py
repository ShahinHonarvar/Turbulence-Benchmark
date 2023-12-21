
import math

def prime_factors(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    integer = lst[1]
    factors = set()
    for i in range(2, integer + 1):
        if integer % i == 0 and is_prime(i):
            factors.add(i)
    return factors
