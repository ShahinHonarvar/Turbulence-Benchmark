import re
def if_perfect_num(nums):
    return bool(re.fullmatch(r"(\d+)", str(nums[0])))
