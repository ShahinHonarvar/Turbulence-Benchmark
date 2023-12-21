
import itertools

def all_left_right_truncatable_prime(x):
    l = itertools.permutations(str(x))
    l = [int(s) for s in l if s[0] != '0' and s[1:] != '0']
    return sorted(l)
