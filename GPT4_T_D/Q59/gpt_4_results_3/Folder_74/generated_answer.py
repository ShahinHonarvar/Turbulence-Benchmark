
from sympy import isprime

def all_left_truncatable_prime(t):
    primes = []
    x = t[36]

    for i in range(10, x):
        str_i = str(i)
        if '0' in str_i:
            continue
        if all(isprime(int(str_i[j:])) for j in range(len(str_i))):
            primes.append(i)
    primes.sort()

    return primes
