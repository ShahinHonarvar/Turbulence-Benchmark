
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[71]

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        num = str(num)
        while len(num) > 0:
            if not isprime(int(num)):
                return False
            num = num[1:]
        return True

    primes = [p for p in range(2, x) if isprime(p) and is_left_truncatable_prime(p)]
    primes.sort(reverse=True)

    return primes
