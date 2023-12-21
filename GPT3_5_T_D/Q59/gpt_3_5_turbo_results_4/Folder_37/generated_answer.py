
from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[35]
    result = []
    for num in count(2):
        if is_prime(num):
            truncatable = True
            for i in range(len(str(num))):
                truncated_num = int(str(num)[i:])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
            if num > x:
                break
    return sorted(result, reverse=True)
