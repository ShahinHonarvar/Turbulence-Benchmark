import itertools
import re
def all_left_truncatable_prime(n):
    return [x for x in PRIMES if all(int(x) == x for x in str(x)) and str(x).lstrip('0') in str(x) for _ in range(1, len(str(x)) + 1)]
