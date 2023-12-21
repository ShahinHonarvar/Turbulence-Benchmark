
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[54]

    def is_left_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(2,x) if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
