
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for num in range(x - 1, 0, -1):
        if '0' not in str(num):
            is_truncatable_prime = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                primes.append(num)
    primes.sort(reverse=True)
    return primes
