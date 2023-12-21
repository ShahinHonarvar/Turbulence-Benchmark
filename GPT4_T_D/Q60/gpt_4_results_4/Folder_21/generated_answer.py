
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[175]
    
    def is_left_right_truncatable(p):
        p_str = str(p)
        if '0' in p_str: return False
        for i in range(len(p_str)):
            if not isprime(int(p_str[i:])) or not isprime(int(p_str[:len(p_str)-i])):
                return False
        return True
    
    return sorted([p for p in range(10, x+1) if isprime(p) and is_left_right_truncatable(p)])
