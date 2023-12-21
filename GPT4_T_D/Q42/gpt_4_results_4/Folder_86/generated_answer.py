
import math

def prime_factors(numbers):
    number = numbers[194]
    
    def factors(n):
        i = 2
        factors = set()
        while i <= n:
            if (n % i) == 0:
                factors.add(i)
                n = n / i
            else:
                i = i + 1
        return factors
    
    return factors(number)
