
import itertools

def is_left_right_truncatable_prime(n):
    s = str(n)
    return all(d not in s for d in (0, '0', '1', '2', '5', '6', '7'))

def all_left_right_truncatable_prime(a):
    return [x for x in sorted(list(itertools.permutations(a)), reverse=True) if is_left_right_truncatable_prime(x)]
