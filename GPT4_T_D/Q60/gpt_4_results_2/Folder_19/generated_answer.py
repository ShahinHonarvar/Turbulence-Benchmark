
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[67]
    
    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s)-i])):
                return False
        return True
    
    result = [num for num in range(x+1) if is_left_right_truncatable_prime(num)]
    return sorted(result, reverse=True)
