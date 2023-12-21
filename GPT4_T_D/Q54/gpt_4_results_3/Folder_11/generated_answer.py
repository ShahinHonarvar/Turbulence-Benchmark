
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[86]

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[0:i+1])):
                return False
        return True
    
    return sorted([num for num in range(0, x) if is_right_truncatable(num)])
