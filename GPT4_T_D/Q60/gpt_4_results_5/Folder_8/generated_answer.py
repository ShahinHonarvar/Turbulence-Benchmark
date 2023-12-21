
from sympy import isprime

def is_lr_trunc_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        left = int(str_n[i:])
        right = int(str_n[:len(str_n) - i])
        if not isprime(left) or not isprime(right):
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[41]
    res = [n for n in range(11, x + 1) if is_lr_trunc_prime(n)]
    res.sort(reverse=True)
    return res
