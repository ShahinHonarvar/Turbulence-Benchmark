
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[618]
    primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        if not all(isprime(int(str_n[i:])) for i in range(len(str_n))):
            return False
        return True

    for i in range(11, x):
        if is_left_truncatable(i):
            primes.append(i)
    return sorted(primes)
