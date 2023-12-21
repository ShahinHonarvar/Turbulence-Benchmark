
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[784]
    res = []
    def left_truncatable_prime(n):
        if n and '0' not in str(n):
            num_str = str(n)
            while num_str:
                if not isprime(int(num_str)):
                    return False
                else:
                    num_str = num_str[1:]
            return True
        else:
            return False
    for i in range(11, x):
        if left_truncatable_prime(i):
            res.append(i)
    return sorted(res)
