
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[975]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    left_truncatable_primes = []
    for number in range(10, x):
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
