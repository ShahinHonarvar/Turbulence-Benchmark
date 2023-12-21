
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[975]
    result = []

    for num in range(x):
        str_num = str(num)
        if all(isprime(int(str_num[:i+1])) for i in range(len(str_num))):
            result.append(num)
    
    return sorted(result, reverse=True)
