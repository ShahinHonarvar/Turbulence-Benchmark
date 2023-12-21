
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[35]
    
    def is_prime(n):
        return isprime(n)
    
    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    
    return sorted([i for i in range(2, x) if is_left_truncatable(i)], reverse=True)
