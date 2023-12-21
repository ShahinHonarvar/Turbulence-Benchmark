
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[61]
    l_prime_nums = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        num_str = str(num)
        flag = True
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                flag = False
                break
        if flag:
            l_prime_nums.append(num)
    return sorted(l_prime_nums)
