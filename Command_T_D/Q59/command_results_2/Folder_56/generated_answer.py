import re
import functools
@functools.lru_cache(maxsize=1_000_000)
def is_left_truncatable_prime(n):
    str_n = str(n)
    return all(n % d == 0 for d in range(2, int(str_n[0])))
def all_left_truncatable_prime(n):
    res = [n for n in range(2, n) if is_left_truncatable_prime(n)]
    res.sort()
    return res
