
from sympy import primerange, isprime

def all_left_truncatable_prime(t):
    x = t[803]
    primes = list(primerange(1, x))
    lt_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        p_str = str(prime)
        left_truncatable = True
        while len(p_str) > 1:
            p_str = p_str[1:]
            if not isprime(int(p_str)):
                left_truncatable = False
                break
        if left_truncatable:
            lt_primes.append(prime)
    return sorted(lt_primes)
