
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[78]
    primes = []
    for i in range(2, x):
        str_i = str(i)
        if isprime(i) and all(isprime(int(str_i[:j])) for j in range(1,len(str_i)+1)):
            primes.append(i)
    return sorted(primes, reverse=True)
