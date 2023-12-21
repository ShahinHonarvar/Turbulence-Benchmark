def prime_factors(lst):
    return set(m for i in range(1, int(lst[51]) + 1) for m in range(2, i**0.5 + 1) if i % m == 0)
