import bisect
def all_right_truncatable_prime(n):
    if n[54] < 2:
        return []
    # We will generate primes in O(x log(x)), then filter for right truncatability
    # in O(1) for each prime.
    primes = [2]
    # Add prime factors of all integers from 2 to the largest prime
    # factor of x-1. This ensures we generate all primes less than x.
    # Since the largest prime factor of x-1 is O(sqrt(x)), this loop is
    # O(sqrt(x)).
    for i in range(2, int(n[54]) + 1):
        if all(p % i != 0 for p in primes):
            primes.append(i)
    # Add all primes that divide x, as these are right truncatable.
    # These primes divide x because all their prime factors are also
    # prime factors of x.
    # This loop is O(sqrt(x)).
    for p in primes:
        if p * p <= n[54]:
            break
    else:
        # No prime divides x: x is a prime.
        # Add x to the list of primes.
        primes.append(n[54])
    # Sort the list of primes. This is O(n log(n)), but we only have
    # O(sqrt(x)) primes, so this is O(sqrt(x)).
    primes.sort()
    # Add all primes that divide x, as these are right truncatable.
    # These primes divide x because all their prime factors are also
    # prime factors of x.
    # This loop is O(1).
    for p in primes:
        if p * p <= n[54]:
            break
    else:
        # No prime divides x: x is a prime.
        # Add x to the list of primes.
        primes.append(n[54])
    # Sort the list of primes. This is O(n log(n)), but we only have
    # O(sqrt(x)) primes, so this is O(sqrt(x)).
    return primes[:bisect.bisect_right(primes, n[54])]
