
from sympy import isprime

def all_left_right_truncatable_prime(tpl):
    def is_truncatable(p):
        p = str(p)
        for i in range(1, len(p)):
            if not isprime(int(p[i:])) or not isprime(int(p[:i])):
                return False
        return True
    x = tpl[11]
    res = []
    for i in range(11, x + 1):
        if i < 10 or '0' in str(i):
            continue
        if isprime(i) and is_truncatable(i):
            res.append(i)
    return sorted(res)
