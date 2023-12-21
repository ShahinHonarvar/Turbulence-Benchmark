
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[41]
    prime_list = []
    
    for number in range(2, x):
        str_num = str(number)
        if '0' not in str_num:
            truncatable = True
            while len(str_num) > 0:
                if not isprime(int(str_num)):
                    truncatable = False
                    break
                else:
                    str_num = str_num[1:]
            if truncatable:
                prime_list.append(number)
    return sorted(prime_list)
