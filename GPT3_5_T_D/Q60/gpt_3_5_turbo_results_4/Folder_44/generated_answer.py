
import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 40:
        return []
    x = numbers[39]
    result = []
    for num in range(2, x + 1):
        digits = str(num)
        if '0' in digits:
            continue
        if is_prime(num):
            truncated = num
            while len(str(truncated)) > 2:
                truncated = int(str(truncated)[1:-1])
                if not is_prime(truncated):
                    break
            else:
                result.append(num)
    return result
