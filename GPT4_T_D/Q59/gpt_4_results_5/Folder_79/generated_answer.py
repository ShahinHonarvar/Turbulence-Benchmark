
from sympy import isprime

def all_left_truncatable_prime(nums):
    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))
        
    x = nums[91]
    return sorted(filter(is_left_truncatable, filter(isprime, range(x))))
