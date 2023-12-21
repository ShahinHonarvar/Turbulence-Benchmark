
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[31]

    def is_truncatable(p):
        p = str(p)
        return all(isprime(int(p[i:])) for i in range(len(p)))

    return sorted([i for i in range(2, x) if '0' not in str(i) and is_truncatable(i)], reverse=True)
