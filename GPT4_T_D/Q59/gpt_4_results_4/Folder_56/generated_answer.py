
from itertools import product
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[30]
    trunc_primes = []
    digits = "123456789"
    
    for i in range(1, len(str(x))):
        for s in product(digits, repeat=i):
            nu = int(''.join(s))
            if nu < x:
                str_nu = str(nu)
                if all(isprime(int(str_nu[j:])) for j in range(len(str_nu))):
                    trunc_primes.append(nu)
    return sorted(trunc_primes)
