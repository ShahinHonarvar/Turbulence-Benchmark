
from sympy import isprime
def all_left_right_truncatable_prime(tuple_of_integers):
    def truncatable(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
            if not isprime(int(str_num[:len(str_num)-i])):
                return False
        return True

    x = tuple_of_integers[100]
    return sorted([i for i in range(10, x+1) if '0' not in str(i) and isprime(i) and truncatable(i)])
