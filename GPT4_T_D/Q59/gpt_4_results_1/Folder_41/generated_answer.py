
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[46]
    lst = []
    for num in range(11, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all(isprime(int(num_str[i:])) for i in range(len(num_str))):
            lst.append(num)
    lst.sort(reverse=True)
    return lst
