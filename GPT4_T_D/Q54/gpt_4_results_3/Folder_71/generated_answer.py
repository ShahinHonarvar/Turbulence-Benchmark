
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[22]
    def is_right_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:i])) for i in range(1, len(s) + 1))
            
    return sorted((n for n in range(x) if is_right_truncatable_prime(n)), reverse=True)
