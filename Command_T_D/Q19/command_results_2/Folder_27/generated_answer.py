import re
def all_ints_not_div_by_num(nums):
    return [n for n in nums[14:21] if not re.fullmatch(r"(-?\d+)/-93", str(n))]
