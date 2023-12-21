
from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    left_truncatables = []
    for i in range(1, x):
        num_str = str(i)
        if '0' in num_str:
            continue
        is_truncatable = True
        while num_str:
            if not is_prime(int(num_str)):
                is_truncatable = False
                break
            num_str = num_str[1:]
        if is_truncatable:
            left_truncatables.append(i)
    return sorted(left_truncatables, reverse=True)
