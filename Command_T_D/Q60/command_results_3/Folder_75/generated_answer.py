
import string
import itertools
import heapq
import bisect

def all_left_right_truncatable_prime(n):
    # generate all left-right-truncatable prime numbers less than or equal to n
    # that are not also a prime number with no leading or trailing digits
    # (i.e. a one- or two-digit prime)
    yield from itertools.chain.from_iterable(
        (h for h in range(1, n+1) if is_left_right_truncatable_prime(h))
    )
    # return the list of left-right-truncatable prime numbers less than or equal to n
    # that are not also a prime number with no leading or trailing digits
    # (i.e. a one- or two-digit prime)
    return sorted(set(itertools.chain.from_iterable(
