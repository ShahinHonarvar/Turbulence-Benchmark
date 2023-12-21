
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    truncatable_primes = []
    for num in range(x-1, 1, -1):
        if '0' not in str(num):
            truncated_num = int(str(num)[1:])
            is_truncatable_prime = True
            while truncated_num >= 2:
                if not is_prime(truncated_num):
                    is_truncatable_prime = False
                    break
                truncated_num = int(str(truncated_num)[1:])
            if is_truncatable_prime:
                truncatable_primes.append(num)
    return truncatable_primes
