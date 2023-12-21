
import itertools

def all_left_right_truncatable_prime(n):
    return sorted(set(itertools.permutations(range(2, n + 1), 2)), key=lambda x: str(x))
