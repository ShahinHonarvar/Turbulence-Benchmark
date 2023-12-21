
import math

def prime_factors(integer_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    if len(integer_list) <= 45:
        return set()
    
    factors = set()
    num = integer_list[45]
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
        if num % (num // i) == 0 and is_prime(num // i):
            factors.add(num // i)
    
    return factors
