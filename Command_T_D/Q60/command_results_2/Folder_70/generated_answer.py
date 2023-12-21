
import re
import itertools

RE = re.compile(r'^(\d[1-9]*)[0-9]*$')

def all_left_right_truncatable_prime(s):
    # Positive integers are left-and-right-truncatable prime
    # if and only if they are prime and left-and-right- truncable
    # hence all such numbers are in the set of primes.
    # Therefore, we can simply call primes and filter.
    # Unfortunately, we can't simply call primes_less_than_or_equal_to
    # since the function may not exist.
    primes = set(range(2, int(s[0])+1))
    return sorted(list(filter(
