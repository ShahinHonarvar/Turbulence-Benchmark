
import sympy

def prime_factors(num_list):
    num = num_list[828]
    factors = sympy.primefactors(num)
    return set(factors)
