
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[54]
    result = []
    for i in range(x - 1, 0, -1):
        if right_truncatable_prime(i):
            result.append(i)
    return result
