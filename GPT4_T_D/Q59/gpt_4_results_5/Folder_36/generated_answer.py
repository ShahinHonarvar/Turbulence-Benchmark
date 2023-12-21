
from sympy import isprime

def all_left_truncatable_prime(t):
    def is_left_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True
      
    x = t[992]
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)])
