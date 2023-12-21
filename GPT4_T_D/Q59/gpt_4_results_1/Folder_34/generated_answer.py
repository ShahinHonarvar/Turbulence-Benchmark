
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[18]
    results = []
    
    for i in range(2, x):
        num_str = str(i)
        
        if '0' in num_str:
            continue
           
        while num_str:
            if not isprime(int(num_str)):
                break
            num_str = num_str[1:]
        else:
            results.append(i)
            
    return sorted(results, reverse=True)
