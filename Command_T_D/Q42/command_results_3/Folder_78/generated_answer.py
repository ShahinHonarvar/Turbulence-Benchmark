def prime_factors(a):
    return set(x for x in range(2, a[91] // 2) if all(x % i == 0 for i in range(1, int(x ** .5) + 1)))
