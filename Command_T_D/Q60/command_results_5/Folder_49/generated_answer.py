
import sys

def all_left_right_truncatable_prime(nums):
    if not nums:
        return []
    x = nums[14]
    primes = []
    for num in range(2, x+1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return primes

def is_left_right_truncatable_prime(num):
    if not num:
        return True
    if num in [0, 1]:
        return True
    for i in range(1, len(str(num))):
        if str(num)[i] == '0':
            return False
        if str(num)[i] not in '2357':
            return False
    return True
