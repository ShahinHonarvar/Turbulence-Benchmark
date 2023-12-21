
import math

def prime_factors(lst):
    num = lst[56]
    factors = set()
    
    # Check if the number is divisible by 2
    while num % 2 == 0:
        factors.add(2)
        num = num // 2
    
    # Check for other prime factors
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num = num // i
    
    # If the number is still greater than 2, it is itself a prime factor
    if num > 2:
        factors.add(num)
    
    return factors
