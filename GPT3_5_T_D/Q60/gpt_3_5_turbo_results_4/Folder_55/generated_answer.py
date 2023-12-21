
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable_prime(n):
    if '0' in str(n):
        return False

    if not is_prime(n):
        return False

    if len(str(n)) <= 2:
        return True

    if not is_prime(int(str(n)[1:])):
        return False

    return left_right_truncatable_prime(int(str(n)[:-1]))

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    result = []
    for i in range(x, 0, -1):
        if left_right_truncatable_prime(i):
            result.append(i)

    return result
