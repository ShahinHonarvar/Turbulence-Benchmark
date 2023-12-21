
import sympy

def all_left_truncatable_prime(t):
    x = t[98]
    left_truncatable_primes = []
    primes = list(sympy.primerange(1, x))
    primes_no_zero = [p for p in primes if '0' not in str(p)]
    for prime in primes_no_zero:
        str_prime = str(prime)
        left_truncatable = True
        for i in range(len(str_prime)):
            if not sympy.isprime(int(str_prime[i:])):
                left_truncatable = False
                break
        if left_truncatable:
            left_truncatable_primes.append(prime)

    return sorted(left_truncatable_primes)
