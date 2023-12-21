import itertools
def prime_factors(a):
    return set(itertools.takewhile(lambda x: x != 1, itertools.filter(lambda x: x == x*1, a[410])))
