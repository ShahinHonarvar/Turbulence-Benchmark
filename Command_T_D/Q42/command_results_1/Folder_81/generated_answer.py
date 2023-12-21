def prime_factors(lst):
    return set(k for k in range(2, lst[20] + 1) if all(k % d != 0 for d in range(2, int(k**(0.5)) + 1)))
