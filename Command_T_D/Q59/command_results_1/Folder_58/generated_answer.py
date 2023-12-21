import bisect
import itertools
import re
def all_left_truncatable_prime(test_tup):
    test_x, = test_tup
    return sorted(set(itertools.takewhile(
        lambda n: all(c in '23579' for c in str(n)),
        bisect.bisect_left(PRIMES, test_x, key=lambda p: str(p)))))
