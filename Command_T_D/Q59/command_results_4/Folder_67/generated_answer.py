import re
import itertools
def all_left_truncatable_prime(tup):
    x = tup[71]
    return sorted(set(PRIMES) - set(n for n in PRIMES if any(n % int(a) == 0 for a in str(n)[:-1])), reverse=True)
