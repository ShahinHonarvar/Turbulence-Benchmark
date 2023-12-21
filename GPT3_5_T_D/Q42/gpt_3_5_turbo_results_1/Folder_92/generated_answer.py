
import math

def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
    
    factors = set()
    num = numbers[0]
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(num // i):
                factors.add(num // i)
    
    return factors
