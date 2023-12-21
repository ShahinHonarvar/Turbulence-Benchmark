
import sys

def all_left_right_truncatable_prime(tup):
    x = tup[6]
    return sorted(set(range(2, x)), key=lambda x: (str(x), x))
