
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[86]
    primes = []
    for num in range(10, x):
        if '0' not in str(num) and isprime(num):
            truncatable = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)
