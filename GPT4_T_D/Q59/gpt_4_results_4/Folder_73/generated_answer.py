
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[97]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(11, x) if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort()
    return left_truncatable_primes
