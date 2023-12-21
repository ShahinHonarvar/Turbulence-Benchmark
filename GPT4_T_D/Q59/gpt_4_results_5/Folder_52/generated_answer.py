
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[52]
    primes = []

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    for i in range(2, x):
        if is_left_truncatable_prime(i):
            primes.append(i)

    return sorted(primes, reverse=True)
