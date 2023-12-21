
from sympy import isprime

def all_left_truncatable_prime(t):
    def left_truncatable(n):
        str_n = str(n)
        if '0' in str(n):
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = t[73]
    primes = list(filter(lambda x: left_truncatable(x), range(2, x)))
    return sorted(primes, reverse=True)
