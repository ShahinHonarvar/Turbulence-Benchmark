
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[22]
    prime_nums = []
    for i in range(2, x):
        str_num = str(i)
        while str_num:
            if isprime(int(str_num)):
                str_num = str_num[:-1]
            else:
                break
        else:
            prime_nums.append(i)
    return sorted(prime_nums, reverse=True)
