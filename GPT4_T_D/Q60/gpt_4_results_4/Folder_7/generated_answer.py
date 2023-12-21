
from sympy import isprime

def truncatable(prime):
    str_prime = str(prime)
    if '0' in str_prime:
        return False
    for i in range(1, len(str_prime)):
        if not isprime(int(str_prime[i:])) or not isprime(int(str_prime[:i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[803]
    res = []
    if x > 13:
        res.extend([2, 3, 5, 7, 13])
        for n in range(17, x + 1):
            if isprime(n) and truncatable(n):
                res.append(n)
    return res
