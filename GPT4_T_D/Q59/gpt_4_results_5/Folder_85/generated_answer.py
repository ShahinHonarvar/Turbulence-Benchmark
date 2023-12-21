
from itertools import chain
from sympy import primerange, isprime

def all_left_truncatable_prime(tup):
    x = tup[94]
    primes = list(primerange(10,x))

    def is_left_truncatable(prime):
        if '0' in str(prime):
            return False
        for i in range(1, len(str(prime))):
            if not isprime(int(str(prime)[i:])):
                return False
        return True

    truncatable_primes = [prime for prime in primes if is_left_truncatable(prime)]
    truncatable_primes.sort()

    return truncatable_primes
