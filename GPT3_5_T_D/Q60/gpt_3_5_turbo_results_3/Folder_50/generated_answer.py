
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[57]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num):
            digits = str(num)
            is_truncatable = True
            for i in range(len(digits)):
                if digits[i] == '0':
                    is_truncatable = False
                    break
                if not is_prime(int(digits[i:])):
                    is_truncatable = False
                    break
                if not is_prime(int(digits[:i+1])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
