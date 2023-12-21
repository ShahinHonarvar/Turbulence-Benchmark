
import itertools

def all_left_right_truncatable_prime(args):
    x, = args
    l = list(range(2, x))
    s = str(l)
    return sorted(list(filter(lambda n: n * 10**9 + 7 > n, itertools.permutations(range(2, int(s[0]) + 1), 2)))))
