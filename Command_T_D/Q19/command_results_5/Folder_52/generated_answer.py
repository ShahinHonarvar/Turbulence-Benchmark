import re
def all_ints_not_div_by_num(nums):
    return [x for x in range(50, 93) if x not in nums and str(x).isdigit()]
