
from sympy import isprime

def all_right_truncatable_prime(tup):
    def right_truncatable_prime(n):
        if n < 2:
            return False
        while n != 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = tup[41]
    result = [i for i in range(2, x) if right_truncatable_prime(i)]
    result.sort()
    return result
