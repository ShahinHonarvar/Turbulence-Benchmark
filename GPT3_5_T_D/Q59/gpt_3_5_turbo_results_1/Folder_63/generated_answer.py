
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    str_n = str(n)
    while len(str_n) > 0:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)
