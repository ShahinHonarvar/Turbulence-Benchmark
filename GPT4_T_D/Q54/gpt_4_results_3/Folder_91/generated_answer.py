
from sympy import isprime

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[0]
    rtp_list = []
    for num in range(2, x):
        str_num = str(num)
        prime_flag = True
        while len(str_num) > 0:
            if isprime(int(str_num)):
                str_num = str_num[:-1]
            else:
                prime_flag = False
                break
        if prime_flag:
            rtp_list.append(num)
    rtp_list.sort(reverse=True)
    return rtp_list
