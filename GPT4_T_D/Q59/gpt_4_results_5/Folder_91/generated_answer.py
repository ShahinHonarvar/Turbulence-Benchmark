
from sympy import isprime

def all_left_truncatable_prime(tuple):
    x = tuple[0]
    
    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(x) if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
