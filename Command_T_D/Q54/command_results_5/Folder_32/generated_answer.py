import itertools
def all_right_truncatable_prime(n):
    # sort of prime numbers
    return sorted(set(itertools.filterfalse(lambda x: all(x % i != 0 for i in range(2, int(x ** .5) + 1)), iter(range(2, int(n) + 1)))))
