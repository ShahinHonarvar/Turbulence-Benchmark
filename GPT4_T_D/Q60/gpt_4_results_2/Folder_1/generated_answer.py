
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[20]
    l_r_primes = []
    for n in range(10, x + 1):
        if '0' in str(n):
            continue
        primes = []
        for i in range(len(str(n))):
            left = int(str(n)[:len(str(n))-i])
            right = int(str(n)[i:])
            if isprime(left) and isprime(right):
                primes.append(n)
        if len(primes)==len(str(n)):
            l_r_primes.append(n)
    return sorted(l_r_primes, reverse=True)
