
import itertools

def all_left_right_truncatable_prime(a):
    b = tuple(str(a[0]))
    return sorted(filter(lambda n: n in a and all(0 not in d for d in str(n)), itertools.permutations(b + ("1", "2"))))
