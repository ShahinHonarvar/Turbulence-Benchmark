import re
def all_ints_not_div_by_num(nums):
    return [x for x in nums if re.fullmatch(r'(\d+)', str(x)) and int(str(x)) % -2]
