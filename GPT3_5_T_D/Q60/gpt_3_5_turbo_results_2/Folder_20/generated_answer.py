
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

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    for i in range(1, len(str(n))):
        left_trunc = int(str(n)[i:])
        right_trunc = int(str(n)[:i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    truncatable_primes = [n for n in range(2, x) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)
