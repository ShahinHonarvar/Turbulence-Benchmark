
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[630]
    rtp_list = []
    for i in range(2, x):
        if isprime(i):
            str_i = str(i)
            rt_prime = True
            while len(str_i) > 1:
                str_i = str_i[:-1]
                if not isprime(int(str_i)):
                    rt_prime = False
                    break
            if rt_prime:
                rtp_list.append(i)
    return sorted(rtp_list, reverse=True)
