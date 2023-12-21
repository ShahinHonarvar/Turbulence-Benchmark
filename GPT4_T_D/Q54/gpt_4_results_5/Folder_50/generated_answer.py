
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[57]
    res = []
    
    def is_right_truncatable_prime(p):
        p = str(p)
        for i in range(len(p)):
            if not isprime(int(p[:len(p)-i])):
                return False
        return True
    
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            res.append(i)
    return sorted(res, reverse=True)
