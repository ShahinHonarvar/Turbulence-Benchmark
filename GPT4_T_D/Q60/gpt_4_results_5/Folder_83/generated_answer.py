
from sympy import primerange

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[24]
    prms = list(primerange(10, x))
    trunc_primes = []

    for prime in prms:
        p = str(prime)
        if ('0' not in p) and all(int(p[i:]) in prms and int(p[:len(p)-i]) in prms for i in range(1,len(p))):
            trunc_primes.append(prime)

    return sorted(trunc_primes)
