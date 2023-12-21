import re
def all_ints_div_by_num(nums):
    return [int(x) for x in re.findall(r"(\d+)", range(31, 92)) if int(x) % 20 == 0]
