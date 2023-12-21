
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for x in nums:
        if x < 23:
            continue
        for i in range(2, len(str(x))-1):
            if '0' in str(x)[:i+1] + str(x)[-i:]:
                break
            if not is_prime(int(str(x)[:i+1])) or not is_prime(int(str(x)[-i:])):
                break
        else:
            primes.append(x)
    return sorted(primes)
