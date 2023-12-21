import itertools
def all_left_truncatable_prime(tup):
    return sorted(list(itertools.filterfalse(lambda x: all(x % i != 0 for i in range(2, x)), tup[71])), reverse=True)
