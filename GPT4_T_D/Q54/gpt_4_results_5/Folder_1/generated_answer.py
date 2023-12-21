
from sympy import *

def all_right_truncatable_prime(t):
    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(isprime(int(str_n[:i+1])) for i in range(len(str_n)))
    x = t[20]
    return sorted(filter(is_right_truncatable_prime, primerange(0,x)), reverse=True)
