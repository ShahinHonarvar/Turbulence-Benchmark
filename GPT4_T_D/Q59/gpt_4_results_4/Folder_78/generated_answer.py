
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[23]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

    return sorted(n for n in range(10, x) if is_left_truncatable_prime(n))
