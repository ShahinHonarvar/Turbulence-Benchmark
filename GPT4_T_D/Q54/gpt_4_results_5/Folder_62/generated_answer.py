
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[70]
    right_truncatable_primes = []

    def is_right_truncatable_prime(num):
        while num:
            if not isprime(num):
                return False
            num //= 10
        return True

    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes)
