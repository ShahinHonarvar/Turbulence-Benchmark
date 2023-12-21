
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[760]

    def is_right_truncatable_prime(n):
        if not isprime(n):
            return False
        if n < 10:
            return True
        return is_right_truncatable_prime(n // 10)

    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
