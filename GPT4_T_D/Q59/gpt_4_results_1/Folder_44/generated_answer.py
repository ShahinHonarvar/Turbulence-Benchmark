
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[39]
    primes = []

    def left_truncatable(prime):
        prime = str(prime)
        if '0' in prime:
            return False
        for i in range(len(prime)):
            if not isprime(int(prime[i:])):
                return False
        return True

    for i in range(10, x):
        if left_truncatable(i):
            primes.append(i)

    return sorted(primes)
