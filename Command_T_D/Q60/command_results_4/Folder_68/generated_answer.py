
import itertools

def all_left_right_truncatable_prime(tup):
    x, = tup
    return sorted(list(set(itertools.takewhile(
