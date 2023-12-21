
from itertools import chain
from sympy import isprime

def all_left_truncatable_prime(num_tup):
    x = num_tup[55]
    if x < 10:
        return []

    primes = ['2', '3', '5', '7']
    for _ in range(1, len(str(x))):
        primes = list(chain(*[['{}{}'.format(p, d) for d in '1379' if isprime(int('{}{}'.format(p, d)))] for p in primes]))

    return sorted(filter(lambda a: int(a) < x, primes), key=int)
