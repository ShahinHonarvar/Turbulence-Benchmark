
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[55]
    primes = list(filter(isprime, range(2, x)))

    left_truncatable_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        truncatable = True
        for i in range(1, len(str(prime))):
            if not isprime(int(str(prime)[i:])):
                truncatable = False
                break
        if truncatable:
            left_truncatable_primes.append(prime)
            
    return sorted(left_truncatable_primes)
