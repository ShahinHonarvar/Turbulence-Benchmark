
from sympy import isprime

def all_left_truncatable_prime(n):
    x = n[61]
    def is_left_truncatable_prime(p):
        if '0' in str(p):
            return False
        return all(isprime(int(str(p)[i:])) for i in range(len(str(p))))
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])
