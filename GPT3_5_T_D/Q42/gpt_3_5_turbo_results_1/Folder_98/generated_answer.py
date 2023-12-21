
from math import isqrt

def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
    
    target_index = 4
    target_number = numbers[target_index]
    factors = set()
    for i in range(2, isqrt(target_number) + 1):
        if target_number % i == 0 and is_prime(i):
            factors.add(i)
    return factors
