
from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def truncate_prime(n: int) -> bool:
    s = str(n)
    for i in range(len(s)):
        if s[i] == '0':
            return False
        if not is_prime(int(s[i:])):
            return False
        if not is_prime(int(s[:i+1])):
            return False
    return True


def all_left_right_truncatable_prime(numbers: tuple) -> list:
    x = numbers[466]
    result = []
    for i in range(x, 9, -1):
        if truncate_prime(i):
            result.append(i)
    return result
