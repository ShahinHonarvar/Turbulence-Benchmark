import itertools
def all_right_truncatable_prime(x):
    return sorted(itertools.takewhile(lambda n: n.is_prime() and n.is_right_truncatable(), range(x - 1)))
