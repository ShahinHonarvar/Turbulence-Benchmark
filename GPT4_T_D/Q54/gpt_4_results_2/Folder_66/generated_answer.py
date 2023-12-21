
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[25]
    rtp_lst = []
    for num in range(1, x):
        num = str(num)
        for i in range(len(num)):
            if not isprime(int(num[i:])):
                break
        else:
            rtp_lst.append(int(num))
    return sorted(rtp_lst, reverse=True)
