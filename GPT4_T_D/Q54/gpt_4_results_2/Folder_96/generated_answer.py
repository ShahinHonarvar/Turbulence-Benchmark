
from sympy import isprime

def all_right_truncatable_prime(t):
    if len(t) < 30:
        return []
    x = t[29]
    def is_right_truncatable_prime(n):
        while n != 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])
