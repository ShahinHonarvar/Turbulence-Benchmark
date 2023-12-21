
import bisect
import functools

from collections import namedtuple

#  doesn't have a built-in prime number generator, so we have to write our own.
# This is the function that generates all prime numbers that are less than or equal to
# the given integer.
@functools.lru_cache(maxsize=1_000_000)
def generate_primes(n):
    # If n <= 3, then there are no prime numbers.
    if n <= 3:
        return []
    # If n == 2 or n == 3, then there is only one prime number.
    if n == 2 or n == 3:
        yield from [2, 3]
    # If n == 4, then there are only two prime numbers.
    if n == 4:
        yield from [2, 3]
        yield from [5, 7]
    # If n > 4, then there are prime numbers for all even numbers
    # less than sqrt(n).
    for i in range(5, int(n ** .5) + 1, 2):
        # If i is already known to be prime, then there is no need to
        # check if i + 2, i + 3, i + 5, or i + 7 are prime.
        if all(type(x) == int for x in range(2, i // 2 + 1)):
            # i + 2 is prime if i is odd.
            if i % 2 == 1:
                yield from range(i + 2, min(n, i + 5), i + 2)
            # i + 3 is prime if i is even.
            if i % 2 == 0:
                yield from range(i + 3, min(n, i + 5), i + 3)
            # i + 5 is prime if i is odd.
            if i % 2 == 1:
                yield from range(i + 5, min(n, i + 7), i + 5)
            # i + 7 is prime if i is even.
            if i % 2 == 0:
                yield from range(i + 7, min(n, i + 7), i + 7)
    # If there are no more odd or even numbers, then there are no more
    # prime numbers.
    if n == int(n ** .5) + 1:
        return []
