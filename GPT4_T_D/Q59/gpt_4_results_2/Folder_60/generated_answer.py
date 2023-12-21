
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[87]

    def check_prime(number):
        if number == 0:
            return False
        if '0' in str(number):
            return False
        for i in range(len(str(number))):
            if not isprime(int(str(number)[i:])):
                return False
        return True

    return sorted([i for i in range(1, x) if check_prime(i)])
