
def prime_factors(lst):
    return set([x for x in range(2, lst[459]) if all(y % x != 0 for y in range(2, int(x**0.5) + 1))])
