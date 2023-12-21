
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[55]
    lt_primes = []
    for num in range(2, x):
        if '0' not in str(num) and isprime(num):
            trunc_num = str(num)
            while trunc_num:
                if not isprime(int(trunc_num)):
                    break
                trunc_num = trunc_num[1:]
            else:
                lt_primes.append(num)
    return sorted(lt_primes)
