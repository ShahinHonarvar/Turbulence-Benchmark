
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[94]
    lst = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num):
            str_num = str(num)
            len_str = len(str_num)
            flag = 0
            for i in range(len_str):
                if not isprime(int(str_num[i:])):
                    flag = 1
                    break
            if flag == 0:
                lst.append(num)
    lst.sort()
    return lst
