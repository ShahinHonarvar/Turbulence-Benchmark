
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

def all_left_truncatable_prime(numbers):
    result = []
    x = numbers[19]
    
    for num in range(11, x):
        if is_prime(num):
            truncatable = True
            digits = str(num)
            for i in range(len(digits)):
                truncated_num = int(digits[i:])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    
    return result
