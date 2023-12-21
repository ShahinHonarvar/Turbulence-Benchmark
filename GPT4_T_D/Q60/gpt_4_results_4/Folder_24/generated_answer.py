
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[65]
    
    def is_truncatable(p):
        str_p = str(p)
        n = len(str_p)
        if '0' in str_p:
            return False
        for i in range(n):
            if not isprime(int(str_p[i:])) or not isprime(int(str_p[:n-i])):
                return False
        return True
    
    truncatable_primes = [p for p in range(10, x+1) if isprime(p) and is_truncatable(p)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
