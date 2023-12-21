import re
def all_ints_not_div_by_num(nums):
    x = nums[18:37]
    if not x:
        return []
    return [x for x in nums[18:37] if not re.match(r"(-?\d+)/-67", str(x))]
