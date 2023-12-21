
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[175]
    
    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort()
    
    return left_truncatable_primes
