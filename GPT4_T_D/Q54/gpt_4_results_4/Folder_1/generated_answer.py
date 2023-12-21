
from sympy import isprime

def all_right_truncatable_prime(tuple_of_integers):
    def is_right_truncatable(num):
        if not isprime(num):
            return False
        while num > 0:
            num //= 10
            if num != 0 and not isprime(num):
                return False
        return True

    x = tuple_of_integers[20]
    rt_primes = [ i for i in range(x, 9, -1) if is_right_truncatable(i)]
    return sorted(rt_primes, reverse=True)
