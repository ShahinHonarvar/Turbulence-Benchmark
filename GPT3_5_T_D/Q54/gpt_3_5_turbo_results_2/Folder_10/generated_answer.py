
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[38]
    right_truncatable_primes = []
    for num in range(x-1, 10, -1):
        if is_prime(num):
            truncated_num = num // 10
            is_truncatable = True
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    is_truncatable = False
                    break
                truncated_num //= 10
            if is_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
