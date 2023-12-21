
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[8]
    right_truncatable_primes = []
    
    def is_right_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True
    
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
            
    return sorted(right_truncatable_primes, reverse=True)
