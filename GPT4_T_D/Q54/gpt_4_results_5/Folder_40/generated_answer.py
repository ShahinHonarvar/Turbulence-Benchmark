
from sympy import isprime

def all_right_truncatable_prime(tup):
    def is_right_truncatable(num):
        while num > 0:
            if not isprime(num):
                return False
            num //= 10
        return True

    x = tup[10]
    return sorted([i for i in range(x) if is_right_truncatable(i)], reverse=True)
