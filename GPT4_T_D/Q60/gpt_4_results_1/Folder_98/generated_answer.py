
from sympy import isprime

def all_left_right_truncatable_prime(t):
    num = t[8]
    res = []
    for n in range(10, num + 1):
        if n % 10 == 0:
            continue
        str_num = str(n)
        for i in range(len(str_num)):
            if not (isprime(int(str_num[i:])) and isprime(int(str_num[:len(str_num)-i]))):
                break
        else:
            res.append(n)
    return sorted(res, reverse=True)
