
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[370]
    truncatable_primes = []
    
    for candidate in range(11, x):
        if '0' in str(candidate):
            continue
            
        primes_found = True
        for i in range(len(str(candidate))):
            if not isprime(int(str(candidate)[i:])):
                primes_found = False
                break
                
        if primes_found:
            truncatable_primes.append(candidate)
            
    return sorted(truncatable_primes, reverse=True)
