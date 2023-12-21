
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(numbers):
    result = []
    x = numbers[28]
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
