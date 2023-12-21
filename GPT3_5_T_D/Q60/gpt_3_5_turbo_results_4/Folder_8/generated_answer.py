
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[41]
    result = []
    for num in range(x, 9, -1):
        if '0' in str(num):
            continue
        temp_num = num
        left_truncatable = True
        right_truncatable = True
        while temp_num > 10:
            temp_num = int(str(temp_num)[1:])
            if not is_prime(temp_num):
                left_truncatable = False
                break
        temp_num = num
        while temp_num > 10:
            temp_num = int(str(temp_num)[:-1])
            if not is_prime(temp_num):
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            result.append(num)
    return sorted(result, reverse=True)
