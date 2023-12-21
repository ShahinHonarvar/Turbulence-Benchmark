
import math

def prime_factors(numbers):
    number = numbers[23]
    factors = set()
    
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.add(i)
            number /= i
    
    if number > 1:
        factors.add(number)
    
    return factors
