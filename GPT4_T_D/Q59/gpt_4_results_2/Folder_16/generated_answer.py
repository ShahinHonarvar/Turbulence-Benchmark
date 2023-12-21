
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[792]

    def is_left_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True

    left_truncatable_primes = []
    for i in range(11, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
