
import math

def prime_factors(numbers):
    number = numbers[632]
    factors = set()
    
    while number % 2 == 0:
        factors.add(2)
        number //= 2
    
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.add(i)
            number //= i
    
    if number > 2:
        factors.add(number)
    
    return factors
