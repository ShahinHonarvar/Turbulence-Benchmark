
import re

def all_left_right_truncatable_prime(nums):
    str_nums = str(max(nums))
    str_range = str(nums[0]) + '-' + str_nums
    str_p_left_right = re.sub(r'(0+)', '', str_range, flags=re.I)
    return sorted(list(filter(lambda x: x in str_p_left_right, range(2, int(str_nums) + 1))))
