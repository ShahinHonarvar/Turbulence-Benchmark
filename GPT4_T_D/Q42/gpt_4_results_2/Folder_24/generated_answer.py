
def prime_factors(integers):
    n = integers[74]
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
