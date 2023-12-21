
from math import isqrt

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[975]
    primes = []
    for i in range(x - 1, 1, -1):
        if '0' in str(i):
            continue
        truncated = str(i)
        while truncated:
            if not is_prime(int(truncated)):
                break
            truncated = truncated[1:]
        else:
            primes.append(i)
    return primes
