
from sympy import isprime

def all_left_truncatable_prime(t):
    def is_left_truncatable_prime(n):
        s = str(n)

        if '0' in s:
            return False

        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False

        return True

    x = t[85]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]

    return sorted(left_truncatable_primes)
