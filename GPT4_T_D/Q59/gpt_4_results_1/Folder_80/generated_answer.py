
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[14]
    left_truncatable_primes = []
    for i in range(10, x):
        if '0' in str(i):
            continue
        ctr = 0
        for j in range(len(str(i))):
            if isprime(int(str(i)[j:])):
                ctr += 1
        if ctr == len(str(i)):
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
