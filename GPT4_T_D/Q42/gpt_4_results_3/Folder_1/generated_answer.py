
def prime_factors(lst):
    n = lst[85]
    factors = set()
    p = 2
    while n >= p * p:
        if n % p:
            p += 1
        else:
            n //= p
            factors.add(p)
    if n > 1:
        factors.add(n)
    return factors
