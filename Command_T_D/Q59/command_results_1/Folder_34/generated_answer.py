import re
import functools
@functools.lru_cache(maxsize=1_000_000)
def is_left_truncatable_prime(n):
    if reg.match(str(n)):
        return False
    s = str(n)
    while s:
        if not all(map(str, range(2, int(s[0])))):
            return False
        s = s[1:]
    return True
def all_left_truncatable_prime(n):
    return sorted(list(range(2, n)), reverse=True)
