
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[46]
    primes = []
    for i in range(2, x):
        if i!=0 and '0' not in str(i):
            if isprime(i):
                s = str(i)
                for j in range(len(s)):
                    if not isprime(int(s[j:])):
                        break
                else:
                    primes.append(i)
    return sorted(primes, reverse=True)
