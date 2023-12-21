
from sympy import isprime

def is_left_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(len(n_str)):
        if not isprime(int(n_str[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[835]
    return sorted(n for n in range(x) if is_left_truncatable_prime(n))
