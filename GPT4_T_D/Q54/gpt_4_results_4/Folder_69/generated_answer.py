
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[760]
    
    rt_primes = []
    for i in range(2, x):
        string_num = str(i)
        is_rt_prime = True
        while len(string_num) > 0:
            if not isprime(int(string_num)):
                is_rt_prime = False
                break
            string_num = string_num[:-1]
        
        if is_rt_prime:
            rt_primes.append(i)
    
    return sorted(rt_primes, reverse=True)
