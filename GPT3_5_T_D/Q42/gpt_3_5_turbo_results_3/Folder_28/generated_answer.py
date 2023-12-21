
import sympy

def prime_factors(numbers):
    integer = numbers[37]
    factors = sympy.primefactors(integer)
    return set(factors)
