import re
def all_pos_ints_inclusive(nums):
    return [x for x in nums if re.fullmatch(r'\d+', str(x))]
