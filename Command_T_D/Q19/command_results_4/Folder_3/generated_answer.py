import re
def all_ints_not_div_by_num(nums):
    return [x for x in range(31, 70) if re.search(r'[+-]70', str(x))]
