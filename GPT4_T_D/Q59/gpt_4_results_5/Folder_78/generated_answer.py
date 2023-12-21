
from itertools import count
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[23]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    return sorted(n for n in count(2) if n < x and is_left_truncatable_prime(n))
