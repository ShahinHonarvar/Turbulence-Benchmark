
import itertools

def all_left_right_truncatable_prime(x):
    return sorted(list(itertools.filter(lambda p: p.ltr_prime(), range(2, x + 1))), reverse=True)
