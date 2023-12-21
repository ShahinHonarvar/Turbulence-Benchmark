import itertools
def all_left_truncatable_prime(n):
    return sorted(list(set(itertools.permutations(range(2, n+1), 2)))), reverse=True)
