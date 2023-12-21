
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if n == 0:
        return []
    primes = []
    for i in range(1, 10):
        num = n * 10 + i
        if is_prime(num):
            primes.append(num)
            primes.extend(left_truncatable_prime(num))
    return primes

def all_left_truncatable_prime(numbers):
    x = numbers[25]
    primes = []
    for i in range(1, 10):
        if is_prime(i):
            primes.append(i)
            primes.extend(left_truncatable_prime(i))
    return sorted(primes, reverse=True)
