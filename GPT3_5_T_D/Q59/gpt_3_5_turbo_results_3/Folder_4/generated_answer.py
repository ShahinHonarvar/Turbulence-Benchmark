
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def truncate_left(num):
    str_num = str(num)
    trunc_nums = []
    for i in range(len(str_num)):
        trunc_nums.append(int(str_num[i:]))
    return trunc_nums

def all_left_truncatable_prime(nums):
    x = nums[96]
    left_trunc_primes = []
    for num in range(x-1, 1, -1):
        if '0' in str(num):
            continue
        trunc_nums = truncate_left(num)
        if all(is_prime(trunc_num) for trunc_num in trunc_nums):
            left_trunc_primes.append(num)
    return sorted(left_trunc_primes, reverse=True)
