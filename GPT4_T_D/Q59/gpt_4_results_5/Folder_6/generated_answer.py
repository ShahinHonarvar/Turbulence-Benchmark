
from sympy import isprime

def all_left_truncatable_prime(values):
    boundary = values[74]

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    return sorted([n for n in range(boundary) if is_left_truncatable_prime(n) and isprime(n)])
