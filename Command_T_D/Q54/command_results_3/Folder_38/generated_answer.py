import itertools
def all_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)),
            itertools.permutations(range(2, int(n) + 1), 3))))
