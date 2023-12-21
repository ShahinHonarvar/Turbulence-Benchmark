
from sympy import isprime

def all_left_truncatable_prime(tup):

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n != 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if str(n)[1:] else 0
        return True

    x = tup[4]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])
