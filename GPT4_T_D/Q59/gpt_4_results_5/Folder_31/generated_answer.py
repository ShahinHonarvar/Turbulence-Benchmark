
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[50]
    def is_left_truncatable_prime(p):
        if '0' in str(p):
            return False
        for i in range(len(str(p))):
            if not isprime(int(str(p)[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)
