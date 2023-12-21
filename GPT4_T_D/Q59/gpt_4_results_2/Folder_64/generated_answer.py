
from sympy import isprime

def all_left_truncatable_prime(nums):
    def left_truncatable_prime(n):
        while n:
            if not isprime(n) or '0' in str(n):
                return False
            n = int(str(n)[1:]) if len(str(n)) > 1 else 0
        return True

    x = nums[4]
    return sorted([i for i in range(10, x) if left_truncatable_prime(i)])
