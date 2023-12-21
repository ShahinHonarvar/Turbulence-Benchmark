
from math import isqrt, sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    right_truncatable_primes = []
    for num in range(x-1, 10, -1):
        if is_prime(num):
            truncatable = True
            temp = num // 10
            while temp > 0:
                if not is_prime(temp):
                    truncatable = False
                    break
                temp = temp // 10
            if truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
