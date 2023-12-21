
from sympy import isprime

def all_left_truncatable_prime(numbers):
    def check_left_truncatable_prime(num):
        if '0' in str(num) or not isprime(num):
            return False
        for i in range(1, len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    x = numbers[33]
    return sorted([i for i in range(1, x) if check_left_truncatable_prime(i)])
