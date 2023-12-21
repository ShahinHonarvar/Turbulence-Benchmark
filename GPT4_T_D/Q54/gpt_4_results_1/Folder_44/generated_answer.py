
from sympy import isprime

def all_right_truncatable_prime(tup):
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = tup[39]
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes)
