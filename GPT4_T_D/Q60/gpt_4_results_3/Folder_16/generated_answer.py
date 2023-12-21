
from itertools import product

def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i, isprime in enumerate(primes):
        if isprime:
            for multiples in range(i*i, n+1, i):
                primes[multiples] = False
    return [prime for prime, checked in enumerate(primes) if checked]

def is_truncatable(prime):
    str_prime = str(prime)
    for i in range(1, len(str_prime)):
        if int(str_prime[i:]) not in primes or int(str_prime[:-i]) not in primes:
            return False
    return True

def all_left_right_truncatable_prime(arg):
    max_number = arg[792]
    global primes
    primes = set(sieve(max_number))
    truncatable_primes = [prime for prime in primes if is_truncatable(prime) and '0' not in str(prime)]
    return sorted(truncatable_primes)
