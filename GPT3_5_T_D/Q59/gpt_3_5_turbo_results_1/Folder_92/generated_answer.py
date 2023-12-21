
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[7]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            trunc_num = str(num)
            while trunc_num != '':
                if not is_prime(int(trunc_num)):
                    is_truncatable = False
                    break
                trunc_num = trunc_num[1:]
            if is_truncatable:
                result.append(num)
    return sorted(result)
