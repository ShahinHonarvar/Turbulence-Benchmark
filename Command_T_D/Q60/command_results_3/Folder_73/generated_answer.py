
import itertools

def all_left_right_truncatable_prime(x):
    return [str(p) for p in sorted(set(itertools.permutations(str(x)) if p != '0' and str(p) in str(x) and str(p) in str(x)[1:-1]))]
