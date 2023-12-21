
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[52]
    def is_left_truncatable_prime(n):
        n_str = str(n)
        if "0" in n_str:
            return False
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True

    truncatable_primes = [i for i in range(2,x) if is_left_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)
