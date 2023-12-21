
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[945]
    
    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        if n < 10:
            return True
        return is_right_truncatable_prime(n//10)
    
    right_truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)
