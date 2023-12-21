
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[618]
    def is_truncatable(p):
        if "0" in str(p): return False
        p = str(p)
        return all(isprime(int(p[i:len(p)-i])) for i in range(len(p)))
    truncatable_primes = [i for i in range(10, x+1) if isprime(i) and is_truncatable(i)]
    return sorted(truncatable_primes)
