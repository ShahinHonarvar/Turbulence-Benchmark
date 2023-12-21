
import sympy

def all_left_truncatable_prime(t):
    x = t[760]
    primes = sympy.primerange(10, x)
    trunc_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        prime_str = str(prime)
        while len(prime_str) > 1:
            prime_str = prime_str[1:]
            if not sympy.isprime(int(prime_str)):
                break
        else:
            trunc_primes.append(prime)
    trunc_primes.sort(reverse=True)
    return trunc_primes
