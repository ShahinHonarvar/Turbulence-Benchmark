
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[65]
    primes = []
    for num in range(2, x):
        if isprime(num):
            is_valid = True
            for i in range(len(str(num))):
                if '0' in str(num[i:]) or not isprime(int(str(num[i:]))):
                    is_valid = False
                    break
            if is_valid:
                primes.append(num)
    primes.sort(reverse=True)
    return primes
