
from sympy import isprime

def all_left_truncatable_prime(nums):
    def is_left_trunctable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = nums[61]
    left_truncatable_primes = []
    for num in range(11, x):
        if is_left_trunctable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
