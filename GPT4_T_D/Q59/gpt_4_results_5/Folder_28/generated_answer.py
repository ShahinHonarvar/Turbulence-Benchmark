
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[19]
    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 0:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True

    truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            truncatable_primes.append(i)
            
    return sorted(truncatable_primes)
