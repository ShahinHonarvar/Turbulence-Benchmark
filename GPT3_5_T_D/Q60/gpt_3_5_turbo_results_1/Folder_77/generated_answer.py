
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    return int(str(n)[1:])

def truncate_right(n):
    return n // 10

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if x < 23:
            continue
        if '0' in str(x):
            continue
        if is_prime(x):
            left_truncatable = True
            right_truncatable = True
            left = truncate_left(x)
            right = truncate_right(x)
            while left > 0:
                if not is_prime(left):
                    left_truncatable = False
                    break
                left = truncate_left(left)
            while right > 0:
                if not is_prime(right):
                    right_truncatable = False
                    break
                right = truncate_right(right)
            if left_truncatable and right_truncatable:
                result.append(x)

    return sorted(result, reverse=True)
