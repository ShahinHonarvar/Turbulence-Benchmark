
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[975]
    right_truncatable_primes = []
    for i in range(x):
        if isprime(i):
            temp = str(i)
            while len(temp) > 0 and isprime(int(temp)):
                temp = temp[:-1]
            if len(temp) == 0:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
