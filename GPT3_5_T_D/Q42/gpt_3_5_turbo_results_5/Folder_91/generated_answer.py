
import math

def prime_factors(numbers):
    number = numbers[6]
    factors = set()
    
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(number // i):
                factors.add(number // i)
    
    return factors
