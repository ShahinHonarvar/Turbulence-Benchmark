
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[96]
    primes = []
        
    def is_left_truncatable(p):
        if '0' in str(p): return False
        length = len(str(p))
        for i in range(length):
            if not isprime(int(str(p)[i:])):
                return False
        return True
        
    for i in range(2, x):
        if is_left_truncatable(i):
            primes.append(i)
            
    return sorted(primes, reverse=True)
