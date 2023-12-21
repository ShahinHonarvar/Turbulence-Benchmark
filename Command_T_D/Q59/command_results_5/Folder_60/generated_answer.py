import sys
import re
from itertools import takewhile
 pattern = re.compile(r'\A(A-Z){2}0(A-Z){2}')
def is_left_truncatable_prime(n):
    s = str(n)
    while s:
        if not pattern.match(s):
            return False
        s = s[1:]
    return True
def all_left_truncatable_prime(x):
    # Pre-calculation
    first_n_left_truncatable_prime = takewhile(lambda x: is_left_truncatable_prime(x), range(3, x))
    # Execution
    return sorted(first_n_left_truncatable_prime)
