import re
import itertools
def all_right_truncatable_prime(tup):
    x = tup[100]
    if x < len(PRIMES):
        return sorted(itertools.takewhile(lambda p: p < x and re.match(r'^[0-9]*$', str(p)), PRIMES))
    else:
        return []
