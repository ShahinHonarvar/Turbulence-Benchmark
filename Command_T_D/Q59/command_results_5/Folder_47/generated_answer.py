import itertools
def all_left_truncatable_prime(n):
    p = list(map(str, range(2, n[0] + 1)))
    return sorted(set(itertools.permutations(p + [0])))
