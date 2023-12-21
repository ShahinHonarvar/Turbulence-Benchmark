
import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    sqrt = int(math.sqrt(n)) + 1
    for divisor in range(3, sqrt, 2):
        if n % divisor == 0:
            return False
    return True

def left_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[784]
    result = []
    for num in range(10, x):
        if left_truncatable_prime(num):
            result.append(num)
    return sorted(result)
