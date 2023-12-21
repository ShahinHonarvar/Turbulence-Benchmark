
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[88]

    def is_right_trunctable_prime(n):
        if not isprime(n):
            return False
        while n != 0:
            n //= 10
            if n and not isprime(n):
                return False
        return True

    result = [i for i in range(x-1, 9, -1) if is_right_trunctable_prime(i)]
    return sorted(result, reverse=True)
