import itertools
def all_right_truncatable_prime(n):
    return sorted(list(itertools.takewhile(lambda n: all(n % d == 0 or n % d == d for d in range(2, int(n ** .5) + 1)), iter(range(2, n - 1)))))
