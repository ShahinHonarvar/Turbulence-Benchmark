import re
def all_ints_not_div_by_num(nums):
    return [int(x) for x in nums[8:-1] if not re.fullmatch(r"(\d+)", str(x))]
