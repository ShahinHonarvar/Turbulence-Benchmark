
import math

def prime_factors(numbers):
    num = numbers[33]
    factors = set()
    
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors.add(i)
            num = num / i
    
    if num > 1:
        factors.add(num)
    
    return factors
