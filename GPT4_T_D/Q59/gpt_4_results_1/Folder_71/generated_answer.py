
from sympy import isprime

def all_left_truncatable_prime(tup):
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        length = len(str(n))
        for i in range(length):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    x = tup[22]
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]

    return sorted(left_truncatable_primes, reverse=True)
