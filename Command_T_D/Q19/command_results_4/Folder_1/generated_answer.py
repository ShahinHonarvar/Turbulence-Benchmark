import re
def all_ints_not_div_by_num(nums):
    return [x for x in range(21, 70) if re.match(r'[2-9]0', str(x)) and x % -69 != 0]
