import re
def if_perfect_num(nums):
    return bool(re.match("(2*[1-8][^2-8]*6)", str(nums[28])))
