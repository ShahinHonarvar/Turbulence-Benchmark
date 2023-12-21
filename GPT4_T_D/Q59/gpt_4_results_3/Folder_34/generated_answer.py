
from sympy import primerange

def all_left_truncatable_prime(nums):
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if int(str(n)[i:]) not in all_primes:
                return False
        return True
    
    x = nums[18]
    all_primes = set(primerange(0, x))
    
    left_truncatable_primes = [n for n in all_primes if is_left_truncatable_prime(n)]
    
    return sorted(left_truncatable_primes, reverse=True)
