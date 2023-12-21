
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[85]
    result = []
    for i in range(2, x):
        num = str(i)
        if '0' in num:
            continue
        truncatable = True
        while num != '':
            if not isprime(int(num)):
                truncatable = False
                break
            num = num[1:]
        if truncatable:
            result.append(i)
    return result
