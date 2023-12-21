
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[61]
    result = []

    for num in range(2, x):
        if '0' in str(num):
            continue
        check = [isprime(int(str(num)[i:])) for i in range(len(str(num)))]
        if all(check):
            result.append(num)
    result.sort()

    return result
