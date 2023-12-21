
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[55]
    primes = []
    def is_right_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[:i])) for i in range(1, len(str_n)+1))
    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)
    return sorted(primes)
