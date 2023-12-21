
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[52]
    truncatable_primes = []
    for i in range(2, x):
        s = str(i)
        for j in range(len(s)):
            if not isprime(int(s[j:])):
                break
        else:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
