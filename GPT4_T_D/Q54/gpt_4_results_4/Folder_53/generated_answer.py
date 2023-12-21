
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[86]
    res = []

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True

    for number in range(2, x):
        if is_right_truncatable_prime(number):
            res.append(number)

    return sorted(res, reverse=True)
