
from sympy import isprime

def all_left_truncatable_prime(numbers):
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    upper_limit = numbers[177]
    return sorted([num for num in range(2, upper_limit) if is_left_truncatable_prime(num)])
