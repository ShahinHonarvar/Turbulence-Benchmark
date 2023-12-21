
from itertools import takewhile
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[84]
    rt = filter(lambda n: isprime(n) and all(isprime(int(format(n, 'd')[:num])) 
    for num in range(1, len(format(n, 'd')) + 1)), range(2, x))
    return sorted(rt, reverse=True)
