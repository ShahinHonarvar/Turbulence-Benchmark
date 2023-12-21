
from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 2:
            n = int(str(n)[1:-1])
            if not isprime(n):
                return False
        return True

    x = nums[43]
    truncatable_primes = [num for num in range(2, x+1) if isprime(num) and is_left_right_truncatable(num)]

    return sorted(truncatable_primes)
