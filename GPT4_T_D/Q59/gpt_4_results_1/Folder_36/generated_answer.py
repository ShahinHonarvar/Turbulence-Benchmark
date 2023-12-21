
from sympy import isprime

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[992]
    res = []
    for i in range(2, x):
        s = str(i)
        if '0' in s:
            continue
        else:
            n = len(s)
            left_truncatable = True
            while n > 0:
                if not isprime(int(s[:n])):
                    left_truncatable = False
                    break
                n -= 1
            if left_truncatable:
                res.append(i)
    return sorted(res)
