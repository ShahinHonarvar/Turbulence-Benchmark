
import math

def prime_factors(numbers):
    integer = numbers[20]
    factors = set()
    
    while integer % 2 == 0:
        factors.add(2)
        integer = integer // 2
    
    for i in range(3, int(math.sqrt(integer)) + 1, 2):
        while integer % i == 0:
            factors.add(i)
            integer = integer // i
    
    if integer > 2:
        factors.add(integer)
    
    return factors
