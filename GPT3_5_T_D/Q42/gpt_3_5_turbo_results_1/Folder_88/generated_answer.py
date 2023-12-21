
import math

def prime_factors(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    integer = numbers[46]
    factors = set()
    
    for i in range(2, int(math.sqrt(integer)) + 1):
        if integer % i == 0 and is_prime(i):
            factors.add(i)
    
    return factors
