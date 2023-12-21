
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[100]

    def is_left_truncatable_prime(n):
        return isprime(n) and all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n) and '0' not in str(n)]
    left_truncatable_primes.sort(reverse=True)

    return left_truncatable_primes
