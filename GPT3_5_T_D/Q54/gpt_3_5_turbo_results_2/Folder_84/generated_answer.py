
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[630]
    result = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            num = str(i)
            while num:
                if not is_prime(int(num)):
                    break
                num = num[:-1]
            else:
                result.append(i)
    return result
