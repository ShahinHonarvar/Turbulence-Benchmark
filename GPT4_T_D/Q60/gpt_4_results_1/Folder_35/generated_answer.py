
from sympy import isprime

def left_right_truncatable(n):
    s = str(n)
    if '0' in s:
        return False

    for i in range(len(s)):
        if not isprime(int(s[i:])):
            return False
        if not isprime(int(s[:len(s)-i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[177]
    return sorted([n for n in range(2, x + 1) if left_right_truncatable(n)])
