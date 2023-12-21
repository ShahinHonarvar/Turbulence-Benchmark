
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_prime(num):
    num_str = str(num)
    if not is_prime(num):
        return False
    while len(num_str) > 1:
        num_str = num_str[:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[1]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
