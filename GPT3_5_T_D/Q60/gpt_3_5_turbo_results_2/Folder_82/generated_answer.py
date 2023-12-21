
from math import sqrt

def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False

        digits = str(n)
        for i in range(len(digits)):
            if not is_prime(int(digits[i:])) or not is_prime(int(digits[:i+1])):
                return False
        return True

    x = numbers[69]
    truncatable_primes = []
    for n in range(x, 1, -1):
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
    
    return truncatable_primes
