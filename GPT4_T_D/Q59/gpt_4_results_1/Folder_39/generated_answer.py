
from sympy import isprime

def all_left_truncatable_prime(t):
    def check_all(i):
        j = str(i)
        while len(j) > 0:
            if not isprime(int(j)):
                return False
            j = j[1:]
        return True
        
    x = t[30]
    lt_primes = []
    for i in range(2, x):
        if '0' not in str(i) and check_all(i):
            lt_primes.append(i)
    return sorted(lt_primes, reverse=True)
