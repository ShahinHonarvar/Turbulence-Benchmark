
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[22]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    sorted_list = sorted(left_truncatable_primes, reverse=True)
    return sorted_list
