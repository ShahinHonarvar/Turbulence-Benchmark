import re
def all_ints_not_div_by_num(nums):
    return [i for i in nums[43:77] if not re.match(r'^84\b', str(i))]
