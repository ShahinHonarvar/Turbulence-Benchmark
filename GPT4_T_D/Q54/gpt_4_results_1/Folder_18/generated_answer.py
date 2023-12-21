
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[429]
    right_truncatable_primes = []
    for i in range(2, x):
        num = str(i)
        while num:   
            if isprime(int(num)):
                num = num[:-1]
            else:
                break
        else:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
