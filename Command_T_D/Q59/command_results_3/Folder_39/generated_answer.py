import itertools
def all_left_truncatable_prime(tup):
    return sorted(list(itertools.takewhile(lambda x: all(x % d == 0 or x % d == 1 for d in range(2, x.bit_length() + 1)), x)), reverse=True)
