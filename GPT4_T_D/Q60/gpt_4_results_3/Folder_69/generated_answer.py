
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[760]
    primes, results = [], []
    for i in range(2, x+1):
        if isprime(i) and '0' not in str(i):
            primes.append(i)
    for prime in primes:
        for i in range(1, len(str(prime))):
            if not (isprime(int(str(prime)[i:])) and isprime(int(str(prime)[:-i]))):
                break
        else:
            results.append(prime)
    return sorted(results, reverse=True)
