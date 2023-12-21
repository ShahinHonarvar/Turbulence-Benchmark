
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[100]
    
    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    
    return sorted(filter(is_left_truncatable, filter(isprime, range(2, x))), reverse = True)
