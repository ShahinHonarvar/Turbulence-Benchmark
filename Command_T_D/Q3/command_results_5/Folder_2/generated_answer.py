import re
def all_pos_ints_inclusive(nums):
    str_nums = " ".join(str(x) for x in nums)
    return re.findall(r"(\d+)((?:[1-9][0-9]*)\d+)", str_nums)
