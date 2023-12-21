
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[57]
    def check_truncatable(prime):
        str_prime = str(prime)
        for i in range(len(str_prime)):
            if not isprime(int(str_prime[i:])):
                return False
        return True
    
    truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and isprime(num):
            if check_truncatable(num):
                truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
