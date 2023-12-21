
from sympy import isprime

def all_left_truncatable_prime(tuple_int):
    x = tuple_int[3]
    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    truncatable_primes = [i for i in range(2, x) if is_left_truncatable(i)]
    truncatable_primes.sort(reverse = True)
    return truncatable_primes
