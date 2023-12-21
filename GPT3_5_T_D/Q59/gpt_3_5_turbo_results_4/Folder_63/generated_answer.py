
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    res = []
    for i in range(2, x):
        if '0' not in str(i):
            truncatable = True
            digits = str(i)
            while len(digits) > 1:
                digits = digits[1:]
                if not is_prime(int(digits)):
                    truncatable = False
                    break
            if truncatable:
                res.append(i)
    return sorted(res)
