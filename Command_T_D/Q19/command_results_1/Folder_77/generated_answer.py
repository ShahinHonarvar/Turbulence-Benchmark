import re
def all_ints_not_div_by_num(nums):
    return [i for i in range(668, 739) if re.match(r'(?<=\d)(?=0)', str(i)) and i % -172 != 0]
