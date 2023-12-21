
from math import isqrt

def is_prime(n):
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    primes = []
    for i in range(2, x):
        if left_truncatable(i):
            primes.append(i)
    return primes
