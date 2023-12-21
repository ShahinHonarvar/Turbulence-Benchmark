
from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[69]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            truncatable = True
            trunc = str(i)
            while trunc:
                if not is_prime(int(trunc)):
                    truncatable = False
                    break
                trunc = trunc[1:]
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
