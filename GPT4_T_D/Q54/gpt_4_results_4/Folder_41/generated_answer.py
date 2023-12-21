
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[46]
    def is_right_truncatable(number):
        if not isprime(number):
            return False
        elif number < 10:
            return True
        else:
            return is_right_truncatable(number // 10)
    return sorted(filter(is_right_truncatable, range(23, x)), reverse=True)
