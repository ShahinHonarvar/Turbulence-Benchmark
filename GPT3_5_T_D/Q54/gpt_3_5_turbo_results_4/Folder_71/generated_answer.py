 
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def truncate_right(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[22]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and truncate_right(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
