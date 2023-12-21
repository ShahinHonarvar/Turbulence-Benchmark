
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[50]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_left_truncatable = True
        for idx in range(len(str_num)):
            if not isprime(int(str_num[idx:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
