
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[14]    
    lp_list = []
    for num in range(11, x):
        if str(num)[0] != '0' and isprime(num):
            truncatable = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])):
                    truncatable = False
                    break
            if truncatable:
                lp_list.append(num)
    return sorted(lp_list, reverse=True)
