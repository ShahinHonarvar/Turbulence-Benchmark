
import itertools

def all_left_right_truncatable_prime(n):
    return sorted(x for x in itertools.permutations(str(n), len(str(n)) - 2) if all(int(x) for x in str(x)))
