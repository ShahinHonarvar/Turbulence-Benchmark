
def prime_factors(lst):
    factors = set()
    if len(lst) > 790:
        n = lst[790]
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
    return factors
