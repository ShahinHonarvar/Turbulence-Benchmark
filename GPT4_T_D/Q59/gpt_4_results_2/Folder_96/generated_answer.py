
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[29]
    
    def is_left_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True
    
    left_truncatable_primes = []
    for i in range(11, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
