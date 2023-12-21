import re
def all_ints_not_div_by_num(nums):
    return [x for x in nums[13:76] if not re.fullmatch(r'44\*', str(x))]
