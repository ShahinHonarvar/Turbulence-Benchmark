
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[70]
    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str(n):
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    return sorted([n for n in range(11, x) if is_left_truncatable_prime(n)])
