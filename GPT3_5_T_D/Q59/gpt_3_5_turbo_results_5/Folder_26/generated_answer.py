
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[81]
    primes = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num):
            continue
        truncated_num = num
        is_truncatable_prime = True
        while truncated_num > 0:
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
            truncated_num //= 10
        if is_truncatable_prime:
            primes.append(num)
    return primes
