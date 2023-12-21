
from itertools import permutations
from sympy import isprime

def all_left_truncatable_prime(t):
    def is_left_truncatable_prime(n):
        if any(c for c in str(n) if c == '0'): return False
        while n != 0:
            if not isprime(n): return False
            n //= 10
        return True

    x = t[466]
    primes = [n for n in range(x) if is_left_truncatable_prime(n)]
    primes.sort(reverse=True)
    return primes
