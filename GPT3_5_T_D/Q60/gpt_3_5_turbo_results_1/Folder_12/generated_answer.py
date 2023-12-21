
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    for _ in range(len(s)):
        if not is_prime(int(s)):
            return False
        s = s[1:]
    s = str(n)
    for _ in range(len(s)):
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    result = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
