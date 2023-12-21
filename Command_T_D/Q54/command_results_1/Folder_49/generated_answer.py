import itertools
def all_right_truncatable_prime(n):
    return sorted(set(itertools.takewhile(lambda x: all(x % d == 0 for d in range(2, x//2 + 1)), itertools.permutations(str(x)))))
