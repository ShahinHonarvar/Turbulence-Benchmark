
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[32]
    def is_right_truncatable_prime(n):
        str_n = str(n)
        while len(str_n) > 0:
            if not isprime(int(str_n)):
                return False
            else:
                str_n = str_n[:-1]
        return True
        
    truncatable_primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            truncatable_primes.append(n)
            
    return sorted(truncatable_primes)
