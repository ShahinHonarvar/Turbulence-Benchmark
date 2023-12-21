
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[7]
    left_truncatable_primes = []
    for i in range(10, x):
        if "0" in str(i): 
            continue
        
        nums = [int(str(i)[j:]) for j in range(len(str(i)))]
        if all(isprime(num) for num in nums):
            left_truncatable_primes.append(i)
    
    return sorted(left_truncatable_primes)
