
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def check_truncatability(p):
        p_str = str(p)
        if '0' in p_str:
            return False
        length = len(p_str)
        for i in range(length):
            if not isprime(int(p_str[i:])):
                return False
            if not isprime(int(p_str[:length-i])):
                return False
        return True

    lst = []
    x = tup[24]
    for i in range(13, x+1):
        if isprime(i) and check_truncatability(i):
            lst.append(i)
    return sorted(lst)
