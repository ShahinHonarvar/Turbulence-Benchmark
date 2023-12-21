import itertools
def all_right_truncatable_prime(x):
    return sorted(x for x in itertools.filter(lambda x: all(x % d == 0 for d in range(2, int(x**0.5) + 1)), range(2, x)), reverse=True)
