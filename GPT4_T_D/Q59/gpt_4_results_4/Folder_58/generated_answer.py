
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[975]
    res = []
    for num in range(0, x):
        if '0' in str(num):
            continue
        temp = str(num)
        while len(temp) > 0:
            if not isprime(int(temp)):
                break
            else:
                temp = temp[1:]
        else:
            res.append(num)
    res.sort(reverse=True)
    return res
