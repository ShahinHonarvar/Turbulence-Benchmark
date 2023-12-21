
from typing import List

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers: tuple) -> List[int]:
    x = numbers[88]
    result = []
    for num in range(2, x):
        if not is_prime(num):
            continue
        truncatable = True
        i = 10
        while num % i != num:
            truncated = num // i
            if not is_prime(truncated):
                truncatable = False
                break
            i *= 10
        if truncatable:
            result.append(num)
    return sorted(result)
