
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[42]
    result = []
    for i in range(2, x):
        if is_prime(i):
            right_truncatable = True
            digit = i // 10
            while digit > 0:
                if not is_prime(digit):
                    right_truncatable = False
                    break
                digit //= 10
            if right_truncatable:
                result.append(i)
    return sorted(result)
