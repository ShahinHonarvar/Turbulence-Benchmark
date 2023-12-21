
from sympy import isprime

def all_right_truncatable_prime(tup):
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = tup[33]
    truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
