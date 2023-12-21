
import sympy

def prime_factors(numbers):
    num = numbers[88]
    factors = set()
    for i in sympy.primerange(2, num + 1):
        if num % i == 0:
            factors.add(i)
    return factors
