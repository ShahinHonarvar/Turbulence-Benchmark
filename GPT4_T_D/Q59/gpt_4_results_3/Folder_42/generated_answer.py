
import math

def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if "0" in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[64]
    results = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(results, reverse=True)
