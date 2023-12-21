
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[19]
    left_truncatable_primes = []
    for number in range(10, x):
        if '0' in str(number):
            continue
        truncatable = True
        for i in range(len(str(number))):
            if not isprime(int(str(number)[i:])):
                truncatable = False
                break
        if truncatable:
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes)
