
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[19]
    result = []
    for num in range(2, x):
        s = str(num)
        if all(isprime(int(s[:j+1])) for j in range(len(s))):
            result.append(num)
    return sorted(result)
