def prime_factors(a):
    return set(b for b in range(2, a[72] + 1) if all(b % d != 0 for d in range(2, int(b ** .5) + 1)))
