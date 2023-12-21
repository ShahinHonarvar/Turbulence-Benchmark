
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[88]

    def is_left_truncatable(n):
        s = str(n)
        return all(isprime(int(s[i:])) for i in range(len(s))) and '0' not in s

    return sorted(n for n in range(2, x) if is_left_truncatable(n))
