
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    
    def is_left_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True

    truncatable_primes = [i for i in range(2, x) if is_left_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
