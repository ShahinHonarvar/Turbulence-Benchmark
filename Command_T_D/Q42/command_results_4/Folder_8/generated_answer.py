def prime_factors(lst):
    return set(x for x in range(2, lst[49] // 2 + 1) if lst[49] % x == 0)
