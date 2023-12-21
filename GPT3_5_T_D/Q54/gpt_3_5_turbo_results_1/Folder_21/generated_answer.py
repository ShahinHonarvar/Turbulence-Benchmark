
from typing import Tuple, List

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n: int) -> bool:
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers: Tuple[int]) -> List[int]:
    x = numbers[175]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
