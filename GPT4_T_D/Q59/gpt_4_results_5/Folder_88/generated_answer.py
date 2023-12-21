
from sympy import isprime

def all_left_truncatable_prime(tuple):
    def is_left_truncatable_prime(number):
        if '0' in str(number) or not isprime(number):
            return False
        while number != 0:
            number = number // 10
            if number != 0 and not isprime(number):
                return False
        return True
    x = tuple[93]
    return sorted(num for num in range(2, x) if is_left_truncatable_prime(num))
