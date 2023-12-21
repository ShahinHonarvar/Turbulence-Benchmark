
from sympy import isprime

def all_left_truncatable_prime(t):
    if len(t) < 70:
        return "Index out of range"
    n = t[69]
    
    def is_left_truncatable(p):
        if '0' in str(p):
            return False
        for i in range(len(str(p))):
            if not isprime(int(str(p)[i:])):
                return False
        return True
    
    truncatables = []
    for x in range(11, n):
        if isprime(x) and is_left_truncatable(x):
            truncatables.append(x)
            
    return sorted(truncatables, reverse=True)
