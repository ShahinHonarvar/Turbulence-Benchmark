
from sympy import isprime

def all_left_truncatable_prime(nums):
    if len(nums) <= 89:
        return []
    x = nums[89]
    truncatable_primes = []
    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    for i in range(2, x):
        if "0" not in str(i) and is_left_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
