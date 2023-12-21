import re
def if_perfect_num(nums):
    return bool(re.search(r"^[1-9][0-9]0$", str(nums[43])))
