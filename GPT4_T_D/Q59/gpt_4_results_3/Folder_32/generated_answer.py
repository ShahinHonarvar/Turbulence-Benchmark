
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[42]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    return sorted(filter(is_left_truncatable_prime, range(2, x)))
