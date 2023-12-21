import re
def all_ints_not_div_by_num(nums):
    return [int(x) for x in nums[18:37] if re.fullmatch(r'([-]?\d+)', x) and int(x) % -67]
