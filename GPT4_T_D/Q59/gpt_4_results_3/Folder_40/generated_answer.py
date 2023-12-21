
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[10]

    def is_left_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    left_trunc_primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
        
    return sorted(left_trunc_primes, reverse=True)
