
from sympy import isprime

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[98]
    def is_left_truncatable_prime(n):
        str_num = str(n)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])
