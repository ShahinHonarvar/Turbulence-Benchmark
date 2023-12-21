
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[26]
    lst_primes = []
    
    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    
    for i in range(10, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            lst_primes.append(i)
            
    return sorted(lst_primes)
