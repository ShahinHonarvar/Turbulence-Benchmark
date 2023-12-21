
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if "0" in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[6]
    result = []
    for i in range(1, x):
        if left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
