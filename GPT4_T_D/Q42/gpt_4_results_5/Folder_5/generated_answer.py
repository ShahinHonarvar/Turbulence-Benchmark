
def prime_factors(lst):
    factors = []
    n = lst[67]
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    prime_factors_set = set(factors)
    return prime_factors_set
