def prime_factors(a):
    return set(i for i in range(2, a[21] // 2) if all(a[21] % i == 0 for j in range(2, i // 2)))
