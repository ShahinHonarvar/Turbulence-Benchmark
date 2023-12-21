
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[645]
    primes = []
    
    def check_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    for n in range(2, x):
        if check_left_truncatable(n):
            primes.append(n)
    return sorted(primes)
