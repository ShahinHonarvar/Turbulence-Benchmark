
from itertools import chain
from sympy import isprime


def all_right_truncatable_prime(tup):
    def rtp(n):
        # n is a list of characters
        n = ''.join(n)
        return n and isprime(int(n)) and rtp(n[:-1])

    return sorted(list(filter(rtp, map(list, map(str, chain(*[range(tup[i]) for i in range(len(tup))]))))), key=int, reverse=True) if tup and len(tup) > 39 else []
