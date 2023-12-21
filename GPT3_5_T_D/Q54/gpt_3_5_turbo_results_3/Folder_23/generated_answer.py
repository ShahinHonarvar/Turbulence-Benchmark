
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for i in range(x-1, 1, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result
