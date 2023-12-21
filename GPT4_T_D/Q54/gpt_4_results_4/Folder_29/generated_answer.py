
from sympy import isprime

def all_right_truncatable_prime(tup):
    def check_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True

    x = tup[55]
    right_truncatable_prime = [i for i in range(2, x) if check_right_truncatable(i)]
    return sorted(right_truncatable_prime, reverse=True)
