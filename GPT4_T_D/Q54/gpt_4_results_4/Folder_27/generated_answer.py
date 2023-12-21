
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[79]

    def is_right_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:i])) for i in range(len(s), 0, -1))

    return sorted((i for i in range(x) if is_right_truncatable_prime(i)), reverse=True)
