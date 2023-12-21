
import itertools

def all_left_right_truncatable_prime(n):
    l = list(itertools.permutations(str(n), 2))
    return [n for n in range(2, int(n) + 1) if all(n % int(s) == 0 for s in l)]
