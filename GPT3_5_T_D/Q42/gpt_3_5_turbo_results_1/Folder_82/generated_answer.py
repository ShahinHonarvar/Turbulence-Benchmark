
import math

def prime_factors(numbers):
    num = numbers[83]
    factors_set = set()
    
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors_set.add(i)
            num /= i
    
    if num > 1:
        factors_set.add(int(num))
        
    return factors_set
