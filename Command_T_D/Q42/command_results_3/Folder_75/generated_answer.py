def prime_factors(lst):
    return set(x for x in range(2, lst[0]//2 + 1) if lst[0] % x == 0)
