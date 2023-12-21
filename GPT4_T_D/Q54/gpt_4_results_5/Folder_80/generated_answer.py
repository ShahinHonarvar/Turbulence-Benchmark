
from sympy import isprime

def all_right_truncatable_prime(numbers):
    def is_right_truncatable(num):
        while num > 0:
            if not isprime(num):
                return False
            num //= 10
        return True

    x = numbers[14]
    return sorted([num for num in range(2, x) if is_right_truncatable(num)], reverse=True)
