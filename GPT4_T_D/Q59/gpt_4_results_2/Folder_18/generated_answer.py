
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[429]
    primes = []
    for i in range(11, x):
        str_i = str(i)
        if "0" in str_i:
            continue
        prime_all = True
        for d in range(len(str_i)):
            if not isprime(int(str_i[d:])):
                prime_all = False
                break
        if prime_all:
            primes.append(i)
    primes.sort(reverse=True)
    return primes
