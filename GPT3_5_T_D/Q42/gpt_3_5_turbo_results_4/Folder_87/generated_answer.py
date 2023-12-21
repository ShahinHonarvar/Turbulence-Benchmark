
import math

def prime_factors(integers):
    number = integers[96]
    factors = set()
    
    # Check and divide by 2 until number is odd
    while number % 2 == 0:
        factors.add(2)
        number = number // 2
    
    # Check and divide by odd numbers starting from 3
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            factors.add(i)
            number = number // i
    
    # If number is still greater than 2, it's a prime factor
    if number > 2:
        factors.add(number)
    
    return factors
