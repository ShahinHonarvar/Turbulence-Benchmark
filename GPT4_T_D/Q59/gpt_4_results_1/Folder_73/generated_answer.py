
from sympy import isprime

def all_left_truncatable_prime(t):
    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    x = t[97]
    return sorted(filter(is_left_truncatable_prime, range(2, x)))
