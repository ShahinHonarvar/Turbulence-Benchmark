
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncate(n):
    digits = str(n)
    while len(digits) > 1:
        digits = digits[1:]
        if not is_prime(int(digits)):
            return False
    return True

def right_truncate(n):
    digits = str(n)
    while len(digits) > 1:
        digits = digits[:-1]
        if not is_prime(int(digits)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[93]
    result = []
    for i in range(2, x+1):
        if '0' not in str(i) and is_prime(i) and left_truncate(i) and right_truncate(i):
            result.append(i)
    return result
