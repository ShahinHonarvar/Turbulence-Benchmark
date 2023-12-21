
import sympy

def all_left_truncatable_prime(tup):
    primes = sympy.primerange(10, tup[33])
    left_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        temp_prime = str(prime)
        while len(temp_prime) > 1:
            temp_prime = temp_prime[1:]
            if not sympy.isprime(int(temp_prime)):
                break
        else:
            left_primes.append(prime)
    return sorted(left_primes)
