
import re

def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(1, len(nums) + 1) if re.fullmatch(r'(4|-6)', str(nums[i-1]))]
