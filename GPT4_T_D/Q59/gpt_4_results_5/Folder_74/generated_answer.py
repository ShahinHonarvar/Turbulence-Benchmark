
from sympy import isprime

def all_left_truncatable_prime(numbers):
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    x = numbers[36]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])
