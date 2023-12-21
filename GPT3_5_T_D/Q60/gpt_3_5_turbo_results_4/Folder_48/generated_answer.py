
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def truncatable_prime(n):
    if not is_prime(n):
        return False
    digits = [int(d) for d in str(n)]
    for i in range(1, len(digits)):
        left_truncated = int(''.join(map(str, digits[i:])))
        right_truncated = int(''.join(map(str, digits[:-i])))
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    result = []
    for i in range(2, x + 1):
        if truncatable_prime(i):
            result.append(i)
    return result
