
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    while len(str_n) > 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[50]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
