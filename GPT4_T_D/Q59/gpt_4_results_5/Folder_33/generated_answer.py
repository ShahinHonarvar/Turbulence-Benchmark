
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[945]
    
    def is_left_truncatable(n):
        if '0' in str(n): 
            return False
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    left_truncatable_primes = [i for i in range(1, x) if is_left_truncatable(i)]
    left_truncatable_primes.sort(reverse=True)

    return left_truncatable_primes
