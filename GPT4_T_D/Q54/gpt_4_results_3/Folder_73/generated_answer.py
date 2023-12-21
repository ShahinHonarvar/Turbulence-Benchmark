
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[97]
    truncated_primes = []
    for num in range(2, x):
        str_num = str(num)
        flag = 1
        while len(str_num) > 1:
            str_num = str_num[:-1]
            if not isprime(int(str_num)):
                flag = 0
                break
        if flag and isprime(num):
            truncated_primes.append(num)
    return sorted(truncated_primes)
