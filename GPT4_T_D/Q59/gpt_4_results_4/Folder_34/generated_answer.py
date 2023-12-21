
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[18]
    
    def is_left_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        return True
    return sorted([p for p in range(23, x) if is_left_truncatable_prime(p)], reverse=True)
