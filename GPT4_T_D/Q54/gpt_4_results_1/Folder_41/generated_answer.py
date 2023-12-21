
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[46]
    def check_right_truncatable(number):
        while number > 0:
            if not isprime(number):
                return False
            number //= 10
        return True

    right_truncatable_primes = [number for number in range(2, x) if check_right_truncatable(number)]

    return sorted(right_truncatable_primes, reverse=True)
