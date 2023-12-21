
from sympy import isprime

def all_right_truncatable_prime(t):
    def is_right_truncatable(n):
        n = str(n)
        while len(n) > 0:
            if not isprime(int(n)):
                return False
            n = n[:-1]
        return True

    x = t[39]
    return sorted([i for i in range(x) if is_right_truncatable(i)], reverse=True)
