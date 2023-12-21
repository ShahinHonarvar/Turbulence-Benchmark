
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[70]
    rt_primes = []
    for num in range(2, x):
        str_num = str(num)
        rt_prime = all(isprime(int(str_num[:i])) for i in range(len(str_num), 0, -1))
        if rt_prime:
            rt_primes.append(num)
    return sorted(rt_primes)
