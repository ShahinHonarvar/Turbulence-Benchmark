
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[41]

    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        while n != 0:
            n //= 10
            if n != 0 and not isprime(n):
                return False
        return True

    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
