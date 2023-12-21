
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[97]
    def is_left_truncatable_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        while n > 0:
            n = n // 10
            if n > 0 and not isprime(n):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)
