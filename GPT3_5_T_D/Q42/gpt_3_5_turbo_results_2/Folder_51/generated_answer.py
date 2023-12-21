
def prime_factors(lst):
    n = lst[64]
    factors = set()
    
    while n % 2 == 0:
        factors.add(2)
        n = n // 2
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n = n // i
        else:
            i += 2
    
    if n > 2:
        factors.add(n)
    
    return factors
