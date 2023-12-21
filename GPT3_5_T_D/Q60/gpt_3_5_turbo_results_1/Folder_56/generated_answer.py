
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if num < 11:
            continue
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        truncatable = True
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
                truncatable = False
                break
        if truncatable:
            primes.append(num)
    primes.sort()
    return primes
