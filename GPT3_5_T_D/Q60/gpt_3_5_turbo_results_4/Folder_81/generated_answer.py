
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    digits = str(n)
    for i in range(1, len(digits)):
        if not is_prime(int(digits[i:])):
            return False
        if not is_prime(int(digits[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[98]
    truncatable_primes = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
