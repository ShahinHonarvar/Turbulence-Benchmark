import re
def if_perfect_num(nums):
    return bool(re.match(".*(1[1-8]23456789)0", str(nums[41])))
