
from math import isqrt

def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[87]
    primes = []
    for i in range(11, x):
        if '0' in str(i):
            continue
        truncatable = True
        num = str(i)
        while num:
            if not is_prime(int(num)):
                truncatable = False
                break
            num = num[1:]
        if truncatable:
            primes.append(i)
    return primes
