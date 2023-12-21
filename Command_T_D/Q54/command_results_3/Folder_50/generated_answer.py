import re
import itertools
def all_right_truncatable_prime(n):
    return sorted(list(set(itertools.filter(lambda x: re.fullmatch(r'[1-9][0-9]*', str(x)), range(1, n[0] + 1))), reverse=True))
