
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[89]
    result = []
    for i in range(2, x):
        num = str(i)
        while num:
            if not is_prime(int(num)):
                break
            num = num[:-1]
        else:
            result.append(i)
    return sorted(result, reverse=True)
