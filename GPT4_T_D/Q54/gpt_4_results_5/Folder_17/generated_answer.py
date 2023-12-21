
from sympy import isprime

def right_truncatable(n):
    n = str(n)
    for i in range(len(n)):
        if not isprime(int(n[i:])):
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[36]
    right_truncatable_primes = [i for i in range(2, x) if right_truncatable(i)]
    return sorted(right_truncatable_primes, reverse=True)
