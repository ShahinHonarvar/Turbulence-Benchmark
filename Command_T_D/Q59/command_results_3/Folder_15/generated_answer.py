import itertools
def all_left_truncatable_prime(n):
    primes = set(range(2, n))
    left_ truncatable_primes = set()
    for p in primes:
        while p:
            if p not in left_truncatable_primes:
                left_truncatable_primes.add(p)
            p //= 10
    return list(left_truncatable_primes)
