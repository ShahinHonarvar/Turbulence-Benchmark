
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[29]

    def is_truncatable(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        for i in range(1, len(str_p)):
            if not isprime(int(str_p[i:])) or not isprime(int(str_p[:-i])):
                return False
        return True

    return sorted(p for p in range(10, x+1) if isprime(p) and is_truncatable(p))
