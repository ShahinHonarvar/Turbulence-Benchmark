import itertools
def all_left_truncatable_prime(tup):
    return sorted(list(filter(lambda x: all(x % d == 0 or x % d == 1 for d in range(2, int(str(x)[-1]) + 1)), tup[0])), key=lambda x: -x)
