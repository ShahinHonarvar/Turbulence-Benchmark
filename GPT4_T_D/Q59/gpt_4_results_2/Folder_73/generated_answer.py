
from sympy import isprime

def all_left_truncatable_prime(tp):
    x = tp[97]
    lt_primes = []
    
    for i in range(10, x):
        if '0' not in str(i):
            lt_prime = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[j:])):
                    lt_prime = False
                    break
            if lt_prime:
                lt_primes.append(i)
    
    return sorted(lt_primes)
