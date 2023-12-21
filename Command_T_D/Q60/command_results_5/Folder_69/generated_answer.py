
import sys
import functools
import bisect

sys.setrecursionlimit(10**7)

# functools.lru_cache(maxsize=10**5)


def all_left_right_truncatable_prime(n):
    """
    :type n: tuple
    :rtype: list
    """
    return sorted(
