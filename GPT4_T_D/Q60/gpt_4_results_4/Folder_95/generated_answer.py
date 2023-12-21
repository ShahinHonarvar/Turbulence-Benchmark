
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[77]
    lp = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        len_num = len(str_num)
        left_right_truncatable = True
        for i in range(len_num):
            left_sub_num = int(str_num[i:]) 
            right_sub_num = int(str_num[:len_num-i]) 
            if (not isprime(left_sub_num)) or (not isprime(right_sub_num)):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            lp.append(num)
    return sorted(lp)
