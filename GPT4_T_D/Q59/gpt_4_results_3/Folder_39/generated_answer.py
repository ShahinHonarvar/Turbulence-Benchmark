
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[30]
    lt_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        if isprime(i):
            i_str = str(i)
            for j in range(1, len(i_str)):
                if not isprime(int(i_str[j:])):
                    break
            else:
                lt_primes.append(i)
    lt_primes.sort(reverse=True)
    return lt_primes
