
from sympy import isprime

def all_left_truncatable_prime(tup):
    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True
    x = tup[26]
    return sorted(filter(is_left_truncatable_prime, range(2,x)))
