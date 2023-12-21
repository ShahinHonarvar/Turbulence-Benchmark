
from sympy import isprime

def all_right_truncatable_prime(val_tuple):
    def is_right_truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[0:i+1])):
                return False
        return True

    x = val_tuple[177]
    res = []
    for i in range(2, x):
        if is_right_truncatable(i):
            res.append(i)
    return sorted(res)
