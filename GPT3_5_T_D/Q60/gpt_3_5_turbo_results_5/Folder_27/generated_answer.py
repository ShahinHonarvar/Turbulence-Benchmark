
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        prime = True
        truncatable = True
        digits = str(num)
        for i in range(len(digits)):
            temp_num = int(digits[i:])
            if not is_prime(temp_num):
                truncatable = False
                break
        if truncatable:
            for i in range(len(digits), 0, -1):
                temp_num = int(digits[:i])
                if not is_prime(temp_num):
                    truncatable = False
                    break
        if truncatable:
            result.append(num)
    return sorted(result, reverse=True)
