
from math import isqrt

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[:i])) or not is_prime(int(n[i:])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for num in range(2, x+1):
        if is_prime(num) and is_truncatable_prime(num):
            primes.append(num)
    return primes
