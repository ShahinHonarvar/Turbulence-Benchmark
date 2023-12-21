
import math

def prime_factors(lst):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    num = lst[28]
    factors = set()

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)

    return factors
