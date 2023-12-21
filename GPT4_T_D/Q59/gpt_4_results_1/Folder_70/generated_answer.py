
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[433]
    # Check if a number is left truncatable prime
    def is_left_truncatable_prime(n):
        str_n = str(n)
        # Check if n is a prime number
        if not isprime(n) or '0' in str_n:
            return False
        # Check if each truncation from left is prime
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    # Get all left truncatable primes less than x
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)
