
import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        left_truncate = int(str_num[i:])
        right_truncate = int(str_num[:i+1])
        if not is_prime(left_truncate) or not is_prime(right_truncate):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[54]
    truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
