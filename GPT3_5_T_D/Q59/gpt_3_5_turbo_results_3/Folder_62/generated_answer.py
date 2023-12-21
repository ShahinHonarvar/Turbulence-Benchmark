
from math import isqrt

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        is_left_truncatable = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(i)
    return result
