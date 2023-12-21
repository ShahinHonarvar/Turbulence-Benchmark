
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[3]
    primes = []
    for i in range(11, x):
        if '0' in str(i):
            continue
        temp = str(i)
        while temp:
            if not isprime(int(temp)):
                break
            temp = temp[1:]
        else:
            primes.append(i)
    return sorted(primes, reverse=True)
