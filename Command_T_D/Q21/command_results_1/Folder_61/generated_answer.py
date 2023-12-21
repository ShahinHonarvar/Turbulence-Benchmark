import re
def all_ints_div_by_num(nums):
    return re.findall(r'[0-9]{%d}'.format(len(str(min(nums)))), range(0, len(nums) + 1))
