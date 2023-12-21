import itertools
def all_left_truncatable_prime(tup):
    x = tup[126]
    return sorted(set(itertools.takewhile(lambda x: all(str(x).count(d) == 1 for d in str(x)), x - 1)))
