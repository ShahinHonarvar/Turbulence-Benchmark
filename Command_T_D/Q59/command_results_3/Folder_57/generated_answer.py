import itertools
import re
def all_left_truncatable_prime(n):
    return sorted(filter(lambda p: p[1] in PRIMES_RE.fullmatch(p[0]), PRIMES), key=lambda p: int(p[1][:p[1].index('0'))))
