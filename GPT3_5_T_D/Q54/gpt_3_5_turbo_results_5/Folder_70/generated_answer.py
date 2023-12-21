
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    limit = isqrt(n) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[433]
    result = []
    for num in range(2, x):
        if is_prime(num):
            successively_removed = str(num)
            while successively_removed:
                if not is_prime(int(successively_removed)):
                    break
                successively_removed = successively_removed[:-1]
            else:
                result.append(num)
    return sorted(result, reverse=True)
