
import math

def all_left_right_truncatable_prime(x):
    return sorted(set(range(2, x, 2)), key=lambda a: -str(a))
