
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[645]
    
    def is_left_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True

    res = [i for i in range(11, x) if is_left_truncatable(i)]
    return sorted(res)
