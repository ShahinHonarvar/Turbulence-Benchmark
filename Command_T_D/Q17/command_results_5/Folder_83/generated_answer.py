
import re

def all_ints_div_by_both_two_nums(nums):
    return [int(i) for i in re.findall(r"(\d+)", nums[90:200]) if i % 13 == i % -31 == 0]
