
import sympy

def prime_factors(lst):
    if len(lst) < 133:
        return set()
    
    num = lst[132]
    factors = sympy.primefactors(num)
    
    return set(factors)
