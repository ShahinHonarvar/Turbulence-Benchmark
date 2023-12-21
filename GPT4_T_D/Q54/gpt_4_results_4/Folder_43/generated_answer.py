
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[89]
    rt_primes = []
    for num in range(0, x):
        str_num = str(num)
        while isprime(num):
            if len(str_num) == 1:
                rt_primes.append(num)
                break
            else:
                str_num = str_num[:-1]
                num = int(str_num)
    rt_primes = sorted(rt_primes, reverse=True)
    return rt_primes
