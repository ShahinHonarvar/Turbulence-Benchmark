
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[61]
    def is_right_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:-i or None])) for i in range(len(s)))

    primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    primes.sort()
    return primes
