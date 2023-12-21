def prime_factors(lst):
    return set(i for i in range(2, lst[29] + 1) if lst[29] % i == 0)
