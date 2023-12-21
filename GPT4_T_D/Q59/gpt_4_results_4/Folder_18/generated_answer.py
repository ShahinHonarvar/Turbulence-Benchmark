
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[429]
    def check_left_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        return True

    truncatable_primes = [n for n in range(2, x) if check_left_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)
