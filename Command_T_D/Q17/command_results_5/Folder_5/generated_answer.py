
import re

def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 2:
        return []
    nums = set(nums)
    return list(re.findall(r"(\d+)", "-6\\*4\\*\\d+"))
