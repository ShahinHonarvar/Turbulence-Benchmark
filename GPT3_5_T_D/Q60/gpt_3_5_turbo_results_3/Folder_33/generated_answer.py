
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if not is_prime(x) or '0' in str(x):
            continue
        x_str = str(x)
        left_truncatable = all(is_prime(int(x_str[:i])) for i in range(1, len(x_str) + 1))
        right_truncatable = all(is_prime(int(x_str[i:])) for i in range(len(x_str), 0, -1))
        if left_truncatable and right_truncatable:
            primes.append(x)
    primes.sort(reverse=True)
    return primes
