import re
def if_perfect_num(nums):
    return re.fullmatch(r"(6\d|8\d|9\d)$", str(nums[685])).group()
