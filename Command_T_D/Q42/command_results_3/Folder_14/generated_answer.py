def prime_factors(a):
    return set(i for i in range(2, a[17] + 1) if all(a[j] % i == 0 for j in range(1, 17)))
