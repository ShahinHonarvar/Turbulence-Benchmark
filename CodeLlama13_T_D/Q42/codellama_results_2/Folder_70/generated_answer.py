
def prime_factors(lst):
    return set([x for x in range(2, 10**5 + 1) if all(y % x == 0 for y in lst)])
