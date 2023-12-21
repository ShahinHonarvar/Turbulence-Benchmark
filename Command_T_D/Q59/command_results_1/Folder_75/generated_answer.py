import sys
def all_left_truncatable_prime(x):
    return sorted(set(x for x in range(2, x) if x.is_prime() and x.rstrip('0') in x))
