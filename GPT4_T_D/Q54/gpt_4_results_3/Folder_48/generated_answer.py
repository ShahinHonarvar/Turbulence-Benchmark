
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[835]
    results = []
    
    def is_right_truncatable(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True
        
    for num in range(2, x):
        if is_right_truncatable(num):
            results.append(num)
            
    return sorted(results)
