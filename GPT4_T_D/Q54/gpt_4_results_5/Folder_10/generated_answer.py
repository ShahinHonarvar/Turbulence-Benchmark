
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[38]
    def truncate(num):
        while num:
            yield num
            num //= 10
      
    trun_primes = []
    for i in range(2, x):
        if all(isprime(x) for x in truncate(i)):
            trun_primes.append(i)
    return sorted(trun_primes, reverse=True)
