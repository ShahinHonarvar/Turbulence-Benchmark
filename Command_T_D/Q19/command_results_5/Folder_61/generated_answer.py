import re
def all_ints_not_div_by_num(nums):
    return [x for x in range(0, 7) if re.search(r'[a-z]d{2}$', str(x)) and x not in nums]
