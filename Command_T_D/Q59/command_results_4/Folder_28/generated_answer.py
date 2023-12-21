import itertools
import re
def all_left_truncatable_prime(n):
    return sorted(n for n in range(2, int(n[19])+1) if all(n%d for d in range(2, int(n) + 1) if not re.match(r'0*', str(n // d))))
