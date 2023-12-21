
import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(nums):
    x = nums[767]
    right_trunc_primes = []
    for i in range(x - 1, 1, -1):
        if right_truncatable_prime(i):
            right_trunc_primes.append(i)
    return sorted(right_trunc_primes, reverse=True)
