
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if '0' in str(n) or not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    primes = []
    for i in range(2, x):
        if left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
