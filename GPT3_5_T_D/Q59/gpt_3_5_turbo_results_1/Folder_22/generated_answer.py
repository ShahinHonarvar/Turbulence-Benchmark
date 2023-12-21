
from math import isqrt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[85]
    result = []
    for i in range(10, x):
        num_str = str(i)
        # Check if the number contains any 0
        if num_str.count('0') > 0:
            continue
        # Check if all left truncations are prime
        is_truncatable_prime = True
        for j in range(1, len(num_str)):
            truncation = int(num_str[j:])
            if not is_prime(truncation):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            result.append(i)
    return result
