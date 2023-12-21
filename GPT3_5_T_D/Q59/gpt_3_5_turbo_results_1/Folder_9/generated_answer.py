
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable_prime = True
            for i in range(1, len(str(num))):
                truncated_num = int(str(num)[i:])
                if not is_prime(truncated_num):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                result.append(num)
    return sorted(result, reverse=True)
