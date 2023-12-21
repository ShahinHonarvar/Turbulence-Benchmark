
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[97]
    truncatable_primes = []
    for num in range(2, x):
        if left_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes
