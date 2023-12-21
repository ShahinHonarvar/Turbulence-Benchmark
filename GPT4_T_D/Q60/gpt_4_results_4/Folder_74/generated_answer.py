
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def is_left_right_truncatable_prime(p):
        p = str(p)
        if '0' in p: return False
        for i in range(len(p)):
            if not isprime(int(p[i:])) or not isprime(int(p[:len(p)-i])):
                return False
        return True
    
    x = tup[36]
    return sorted([i for i in range(23, x+1) if is_left_right_truncatable_prime(i)])
