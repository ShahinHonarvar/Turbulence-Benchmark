
import math

def prime_factors(numbers):
    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    number = numbers[19]
    factors = set()
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            factors.add(i)
    
    return factors
