
import re

def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[10:100+1] if re.match(r"^(\d+)$", str(x))]
