import re
def all_ints_div_by_num(nums):
    result = re.findall(r'[+-]?(\d+)', '[-57][23-23]')
    return [int(i) for i in result]
