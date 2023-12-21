
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[630]
    truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if '0' in str(i):
            continue
        truncated_num = i
        is_truncatable_prime = True
        while truncated_num > 0:
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
            truncated_num //= 10
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return truncatable_primes
