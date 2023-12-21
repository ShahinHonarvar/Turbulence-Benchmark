
import sympy

def prime_factors(lst):
    num = lst[59]
    factors = set(sympy.primefactors(num))
    return factors
