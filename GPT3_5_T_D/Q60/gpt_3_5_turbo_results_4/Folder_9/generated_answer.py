
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    while len(str_n) > 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:-1]
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[29]
    trunc_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            trunc_primes.append(i)
    trunc_primes.sort(reverse=True)
    return trunc_primes
