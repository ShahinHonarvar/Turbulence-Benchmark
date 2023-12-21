
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n < 10:
        return False
    str_num = str(n)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    for i in range(len(str_num) - 1, 0, -1):
        if not is_prime(int(str_num[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[81]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
