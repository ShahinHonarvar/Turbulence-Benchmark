def prime_factors(lst):
    return set(x for x in range(2, int(lst[828]) + 1) if lst[828] % x == 0)
