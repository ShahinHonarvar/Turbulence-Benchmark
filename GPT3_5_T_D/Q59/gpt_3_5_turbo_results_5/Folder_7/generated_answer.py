
from sympy import isprime

def is_left_truncatable_prime(number):
    if '0' in str(number):
        return False
    while number > 0:
        if not isprime(number):
            return False
        number = int(str(number)[1:])
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[803]
    return sorted([num for num in range(2, x) if is_left_truncatable_prime(num)])
