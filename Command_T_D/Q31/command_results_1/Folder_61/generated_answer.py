import re
def if_perfect_num(nums):
    return bool(re.search("(1|2|3|4|5|6|7|8)0$", str(nums[8])))
