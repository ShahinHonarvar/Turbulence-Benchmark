
def prime_factors(lst):
    return set(range(2, int(lst[63]**0.5) + 1)) - set(range(2, int(lst[63]**0.5) + 1, lst[63]))
