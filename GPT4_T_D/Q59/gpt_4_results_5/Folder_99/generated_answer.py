
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[758]
    left_truncatable_primes = []

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    
    for n in range(2, x):
        if is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
    
    return sorted(left_truncatable_primes)
