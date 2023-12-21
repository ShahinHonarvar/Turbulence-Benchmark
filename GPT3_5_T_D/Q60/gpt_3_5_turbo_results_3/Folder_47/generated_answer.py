
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    if not is_prime(n):
        return False
    num_str = str(n)
    while len(num_str) > 1:
        num_str = num_str[1:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[49] if len(numbers) >= 50 else 0
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)
