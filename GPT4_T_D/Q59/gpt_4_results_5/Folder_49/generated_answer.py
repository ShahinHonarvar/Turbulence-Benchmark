
from sympy import isprime

def all_left_truncatable_prime(arr):
    x = arr[14]
    
    def is_left_truncatable_prime(n):
        str_n = str(n)
        if "0" in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    truncatable_primes = [i for i in range(11, x) if is_left_truncatable_prime(i)]
    return sorted(truncatable_primes)
