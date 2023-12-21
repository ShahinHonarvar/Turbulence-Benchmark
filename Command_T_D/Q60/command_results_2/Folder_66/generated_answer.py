
import re

def all_left_right_truncatable_prime(test_args):
    x, = test_args
    primes = set(range(2, int(x ** .5) + 1))
    primes = {str(p) for p in primes if is_left_right_truncatable_prime(p)}
    return sorted(primes)

def is_left_right_truncatable_prime(n):
    if len(str(n)) == 1:
        return True
    return n % 10 == 0 and n not in [0, 1]
