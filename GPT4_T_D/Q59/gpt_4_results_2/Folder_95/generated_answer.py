
from sympy import isprime

def all_left_truncatable_prime(nums):
    def is_left_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True

    x = nums[77]
    return sorted(filter(is_left_truncatable_prime, range(2, x)))
