
from sympy import isprime

def all_left_truncatable_prime(nums: tuple) -> list:
    x = nums[100]
    result = []
    for num in range(10, x):
        if '0' in str(num):
            continue
        is_valid = True
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                is_valid = False
                break
        if is_valid:
            result.append(num)
    result.sort()
    return result
