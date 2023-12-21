
from sympy import isprime

def all_left_truncatable_prime(tup):
    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        str_n_len = len(str_n)
        for i in range(str_n_len):
            if not isprime(int(str_n[i:])):
                return False
        return True
    
    x = tup[1]
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
