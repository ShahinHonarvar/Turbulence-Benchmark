
from sympy import isprime

def all_right_truncatable_prime(nums):
    def is_right_truncatable(num):
        num_str = str(num)
        while len(num_str) > 0:
            if not isprime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    
    x = nums[89]
    return sorted([i for i in range(2, x) if is_right_truncatable(i)], reverse=True)
