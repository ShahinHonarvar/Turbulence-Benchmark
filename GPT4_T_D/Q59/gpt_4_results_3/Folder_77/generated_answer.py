
import sympy

def all_left_truncatable_prime(tup):
    x = tup[767]
    primes = list(sympy.primerange(10, x))
    left_truncatable_primes = []

    for prime in primes:
        if '0' in str(prime):
            continue
        is_prime = True
        for i in range(len(str(prime))):
            if not sympy.isprime(int(str(prime)[i:])):
                is_prime = False
                break
        if is_prime:
            left_truncatable_primes.append(prime)

    return sorted(left_truncatable_primes, reverse=True)
