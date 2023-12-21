
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[79]

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False

        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(x) if is_left_truncatable_prime(i)]

    return sorted(left_truncatable_primes, reverse=True)
