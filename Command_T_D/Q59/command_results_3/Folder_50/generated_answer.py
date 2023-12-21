import itertools
def all_left_truncatable_prime(n):
    return sorted(set(n) for n in itertools.permutations(str(n)) if all(n % i != 0 for i in range(2, int(n) + 1)))
