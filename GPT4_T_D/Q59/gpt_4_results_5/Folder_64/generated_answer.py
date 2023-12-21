
from sympy import isprime

def is_left_truncatable(n):
    n = str(n)
    if '0' in n:
        return False
    N = len(n)
    for i in range(N):
        if not isprime(int(n[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[4]
    left_truncatable_nums = []
    for i in range(2, x):
        if is_left_truncatable(i):
            left_truncatable_nums.append(i)
    return sorted(left_truncatable_nums)
