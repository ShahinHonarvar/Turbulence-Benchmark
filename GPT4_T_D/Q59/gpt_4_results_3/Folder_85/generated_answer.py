
from sympy import isprime

def all_left_truncatable_prime(args):
    x = args[94]
    def is_left_truncatable_prime(p):
        if '0' in str(p):
            return False
        return all(isprime(int(str(p)[i:])) for i in range(len(str(p))))
    return sorted(p for p in range(2, x) if is_left_truncatable_prime(p))
