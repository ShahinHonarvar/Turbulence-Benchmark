
from sympy import isprime

def left_truncatable(p):
    p = str(p)
    for i in range(len(p)):
        if not isprime(int(p[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[81]
    primes = []
    for i in range(2, x):
        if '0' not in str(i) and left_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)
