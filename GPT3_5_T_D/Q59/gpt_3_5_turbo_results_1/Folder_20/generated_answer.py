
from sympy import isprime


def all_left_truncatable_prime(numbers):
    x = numbers[100]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    primes = [i for i in range(2, x) if is_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes
