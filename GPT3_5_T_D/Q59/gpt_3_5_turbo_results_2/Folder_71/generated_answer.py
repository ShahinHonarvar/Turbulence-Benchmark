
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if n == 0:
        return []
    primes = []
    for i in range(1, 10):
        if is_prime(i):
            primes.append(i)
    for i in range(len(primes)):
        if primes[i] < n:
            for j in range(10):
                new_num = 10 * primes[i] + j
                if is_prime(new_num):
                    primes.append(new_num)
    return sorted(primes, reverse=True)


def all_left_truncatable_prime(numbers):
    x = numbers[22]
    return left_truncatable_prime(x)
