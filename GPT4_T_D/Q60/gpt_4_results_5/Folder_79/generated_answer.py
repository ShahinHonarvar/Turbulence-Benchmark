
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[91]
    def is_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
            if not isprime(int(n[:len(n)-i])):
                return False
        return True

    return sorted([n for n in range(10, x+1) if is_truncatable(n)])
