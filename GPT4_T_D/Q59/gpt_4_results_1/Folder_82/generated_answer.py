
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[69]

    def is_left_truncatable_prime(number):
        if '0' in str(number):
            return False
        for i in range(len(str(number))):
            if not isprime(int(str(number)[i:])):
                return False
        return True

    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = [i for i in primes if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
