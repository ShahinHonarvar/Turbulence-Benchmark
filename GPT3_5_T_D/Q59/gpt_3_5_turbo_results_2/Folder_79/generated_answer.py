
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[91]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            is_left_truncatable = True
            for i in range(1, len(str(num))):
                truncated_num = int(str(num)[i:])
                if not is_prime(truncated_num):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
