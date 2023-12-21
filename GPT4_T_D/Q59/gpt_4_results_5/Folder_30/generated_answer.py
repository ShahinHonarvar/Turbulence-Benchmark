
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[37]
    primes = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num):
            is_left_truncatable = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
