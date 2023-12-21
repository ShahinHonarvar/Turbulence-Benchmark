
def prime_factors(lst):
    import sympy
    num = lst[132]
    return set(sympy.factorint(num).keys())
