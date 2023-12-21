
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[98]
    result = []
    for number in range(2, x):
        if '0' not in str(number):
            is_truncatable = True
            for i in range(len(str(number))):
                trunc_number = int(str(number)[i:])
                if not is_prime(trunc_number):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(number)
    return result
