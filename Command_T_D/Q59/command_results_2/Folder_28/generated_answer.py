import sys
import itertools
import bisect
def all_left_truncatable_prime(n):
    # Preprocess data
    primes = [0]
    for i in range(2, n):
        if all(x == '9' for x in str(i)):
            yield i
            continue
        if primes[-1] == 0:
            primes.append(i)
        else:
            j = bisect.bisect_left(primes, i)
            yield from primes[:j]
            primes = [i] + primes[j:]
    yield from primes
def test():
    # Use the function
    n = 10**18
    prime = [1, 3, 5, 7, 11, 13, 17, 19]
    print(*(x for x in all_left_truncatable_prime((n, n-1)) if x in prime))
