def prime_factors(a):
    i = 733
    factors = set()
    while i not in factors:
        if all(x % i == 0 for x in a):
            factors.add(i)
            for x in range(2, i // 2):
                if a[x] == i:
                    factors.add(x)
                    a[x] = 1
        i += 1
    return factors
