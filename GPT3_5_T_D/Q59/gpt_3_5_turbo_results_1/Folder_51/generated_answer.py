
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[54]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            num_str = str(i)
            while num_str:
                if num_str[0] == '0':
                    break
                if not is_prime(int(num_str)):
                    break
                num_str = num_str[1:]
            else:
                primes.append(i)
    return sorted(primes)
