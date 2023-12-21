
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if is_prime(n):
        if n < 10:
            return [n]
        primes = []
        for i in range(1, 10):
            if is_prime(n // 10 + i):
                primes.extend(right_truncatable_prime(n // 10 + i))
        return primes
    return []

def all_right_truncatable_prime(numbers):
    x = numbers[89]
    result = []
    for i in range(2, x):
        if is_prime(i):
            result.extend(right_truncatable_prime(i))
    return sorted(result, reverse=True)
