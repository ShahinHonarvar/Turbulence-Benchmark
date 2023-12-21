
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:(i+1)])):
                return False
        return True

    x = tup[70]
    return sorted(filter(is_left_right_truncatable_prime, range(10, x + 1)))
