
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[70]
    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        n = str(n)
        while len(n) > 1:
            n = n[:-1]
            if not isprime(int(n)):
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
