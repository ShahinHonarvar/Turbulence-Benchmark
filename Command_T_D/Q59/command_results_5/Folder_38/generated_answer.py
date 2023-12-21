import re
import itertools
def all_left_truncatable_prime(test_tup):
    x = test_tup[28]
    return sorted(filter(lambda p: p < x and re.match(r'0*(?=\d)'), PRIMES))
