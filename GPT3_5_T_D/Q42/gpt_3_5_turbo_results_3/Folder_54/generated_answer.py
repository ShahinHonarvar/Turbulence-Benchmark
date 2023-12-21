
import sympy

def prime_factors(integers):
    prime_factors_set = set()
    integer = integers[51]
    factors = sympy.primerange(2, integer)
    
    for factor in factors:
        if integer % factor == 0:
            prime_factors_set.add(factor)
    
    return prime_factors_set
