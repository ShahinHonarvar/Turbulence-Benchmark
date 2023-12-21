
def prime_factors(lst):
    return set([x for x in range(2, lst[714]) if lst[714] % x == 0 and all(y % x != 0 for y in range(2, int(lst[714] ** 0.5) + 1))])
