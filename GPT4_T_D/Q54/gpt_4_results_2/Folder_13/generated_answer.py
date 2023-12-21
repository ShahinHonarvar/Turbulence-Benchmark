
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[784]
    def check_right_truncatable(num):
        while num != 0:
            if not isprime(num):
                return False
            num //= 10
        return True

    return sorted(num for num in range(2, x) if check_right_truncatable(num))
