
import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[54]
    result = []
    
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            for i in range(len(str(num)) - 1):
                truncated_num = int(str(num)[i + 1:])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                result.append(num)
    
    return sorted(result, reverse=True)
