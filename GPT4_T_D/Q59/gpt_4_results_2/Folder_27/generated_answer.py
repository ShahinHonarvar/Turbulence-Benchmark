
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[79]
    def is_left_truncatable(p):
        p = str(p)
        return all(isprime(int(p[i:])) for i in range(len(p)))
    return sorted(filter(is_left_truncatable, range(10, x)), reverse=True)
