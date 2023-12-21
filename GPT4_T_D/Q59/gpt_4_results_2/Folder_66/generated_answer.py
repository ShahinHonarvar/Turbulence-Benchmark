
from sympy import isprime

def all_left_truncatable_prime(tuple_integers):
    x = tuple_integers[25]
    left_truncatable_primes = []

    for i in range(11, x):
        if '0' in str(i):
            continue
        truncatable = True
        for j in range(1, len(str(i))):
            if not isprime(int(str(i)[j:])):
                truncatable = False
                break
        if truncatable and isprime(i):
            left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes, reverse=True)
