import re
def all_ints_div_by_num(nums):
    return re.findall(r"(\d+)", range(30,30+len(nums),3))
