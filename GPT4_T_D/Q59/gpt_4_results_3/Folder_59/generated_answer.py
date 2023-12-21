
from sympy import isprime

def all_left_truncatable_prime(nums):
    def is_left_truncatable_prime(n):
        # Check if all truncated versions are prime
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        # Check for zero in number. If it exists, return false
        if '0' in str(n):
            return False
        return True

    limit = nums[84]
    nums = [x for x in range(2, limit) if is_left_truncatable_prime(x)]
    return sorted(nums, reverse=True)
