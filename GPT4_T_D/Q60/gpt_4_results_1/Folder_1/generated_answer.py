
from sympy import isprime

def check_truncatable(n):
    s = str(n)
    return all(isprime(int(s[i:])) and isprime(int(s[:len(s)-i])) for i in range(len(s)))

def all_left_right_truncatable_prime(nums):
    x = nums[20]
    return sorted([i for i in range(10, x+1) if '0' not in str(i) and check_truncatable(i)], reverse=True)
