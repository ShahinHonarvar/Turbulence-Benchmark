
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    num = str(n)
    while num:
        if not is_prime(int(num)):
            return False
        num = num[1:]
    num = str(n)
    while num:
        if not is_prime(int(num)):
            return False
        num = num[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)
