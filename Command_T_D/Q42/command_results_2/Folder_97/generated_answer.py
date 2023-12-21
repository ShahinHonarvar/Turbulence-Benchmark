def prime_factors(lst):
    return set(x for x in range(2, int(lst[0]) + 1) if lst[0] % x == 0)
