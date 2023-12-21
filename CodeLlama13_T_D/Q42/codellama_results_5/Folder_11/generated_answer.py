
def prime_factors(lst):
    return set([x for x in range(2, int(lst[77])+1) if lst[77] % x == 0 and all(lst[77] % y != 0 for y in range(2, int(x**0.5)+1))])
