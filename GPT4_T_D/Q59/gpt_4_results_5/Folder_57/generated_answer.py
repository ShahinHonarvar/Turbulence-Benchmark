
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[54]
    
    def is_left_truncatable(n):
        if '0' in str(n): 
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    res = []
    for i in range(11, x):
        if is_left_truncatable(i):
            res.append(i)
    return sorted(res, reverse=True)
