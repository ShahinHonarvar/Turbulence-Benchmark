
from sympy import isprime

def left_truncatable(n):
    str_n = str(n)
    if '0' in str_n: 
        return False
    for i in range(len(str_n)):
        if not isprime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[49]
    res = []
    for num in range(11, x):
        if left_truncatable(num):
            res.append(num)
    return sorted(res)
