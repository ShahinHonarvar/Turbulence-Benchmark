
import math

def prime_factors(numbers):
    target_number = numbers[276]
    factors = set()
    
    while target_number % 2 == 0:
        factors.add(2)
        target_number //= 2
    
    for i in range(3, int(math.sqrt(target_number)) + 1, 2):
        while target_number % i == 0:
            factors.add(i)
            target_number //= i
    
    if target_number > 2:
        factors.add(target_number)
    
    return factors
