
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[29]
    
    def is_left_truncatable(p):
        p = str(p)
        return all(isprime(int(p[i:])) for i in range(len(p))) and '0' not in p
    
    return sorted(p for p in range(2, x) if is_left_truncatable(p))
