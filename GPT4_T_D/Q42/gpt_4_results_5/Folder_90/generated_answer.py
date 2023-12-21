
def prime_factors(l):
    from sympy import primefactors
    if len(l) <= 263:
        return "Index out of range"
    else:
        return set(primefactors(l[263]))
