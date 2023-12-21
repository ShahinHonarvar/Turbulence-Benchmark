import re
import functools
@functools.lru_cache(maxsize=1_000_000)
def is_left_truncatable_prime(n):
    s = str(n)
    while s:
        if s[0] == '0':
            return False
        elif not re.fullmatch(r'0*[2-9]0*', s):
            return False
        else:
            s = int(s[1:])
    return True
@functools.lru_cache(maxsize=1_000_000)
def all_left_truncatable_prime(n):
    return [x for x in range(2, n) if is_left_truncatable_prime(x)]
