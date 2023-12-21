
from sympy import isprime

def all_left_truncatable_prime(t):
    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        if not isprime(n):
            return False

        while len(str_n) > 1:
            str_n = str_n[1:]
            if not isprime(int(str_n)):
                return False
        return True
    
    x = t[81]
    return sorted([i for i in range(x) if is_left_truncatable_prime(i)], reverse=True)
