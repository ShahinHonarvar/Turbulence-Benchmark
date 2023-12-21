
import itertools

def all_left_right_truncatable_prime(n):
    l = list(range(2, n))
    return [n for n in l if all(n % d == 0 for d in itertools.drop(l, 1)) and n % 10 in (1, 5, 3, 7)]
