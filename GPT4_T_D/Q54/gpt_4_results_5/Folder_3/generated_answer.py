
from itertools import count
from sympy import isprime

def all_right_truncatable_prime(t):
    def is_right_truncatable_prime(n):
        n = str(n)
        return all(isprime(int(n[:i+1])) for i in range(len(n)))

    x = t[100]
    primes = []
    for i in count(1):
        if i >= x:
            break
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)
