
from sympy import isprime

def all_right_truncatable_prime(nums):
    def is_right_truncatable_prime(n):
        n = str(n)
        return all(isprime(int(n[i:])) for i in range(len(n)))
        
    x = nums[77]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])
