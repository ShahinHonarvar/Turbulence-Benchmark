import re
def all_ints_not_div_by_num(nums):
    if len(nums) == 0:
        return []
    return [x for x in nums if not re.match(r"(\d+)[13579]0", str(x))]
