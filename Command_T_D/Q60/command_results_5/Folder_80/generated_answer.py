
import re
import itertools
import functools

@functools.lru_cache(maxsize=1_000_000)
def get_left_right_ truncatable_primes(n):
    # adapted from https://www.codewars.com/kata/reviews/53d0c5c07/groups/5590
    # your code here
    if n < 2:
        return []
    if n <= 1_000:
        return [str(n)]
    if n <= 9_999:
        return [str(n)] + get_left_right_truncatable_primes(n-1)
    # otherwise
    # start by generating all left-and-right-truncatable prime numbers less than n
    return get_left_right_truncatable_primes(n-1) + [str(n)]

@functools.lru_cache(maxsize=1_000_000)
def is_left_right_truncatable_prime(s):
    # adapted from https://www.codewars.com/kata/reviews/53d0c5c07/groups/5590
    # your code here
    return re.fullmatch(r'(?P<a>[0-9])\d+\1', s)

@functools.lru_cache(maxsize=1_000_000)
def all_left_right_truncatable_prime(n):
    # adapted from https://www.codewars.com/kata/reviews/53d0c5c07/groups/5590
    # your code here
    a = get_left_right_truncatable_primes(n)
    return [x for x in a if is_left_right_truncatable_prime(x)]
