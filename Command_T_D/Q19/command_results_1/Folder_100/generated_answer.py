import re
def all_ints_not_div_by_num(nums):
    return [x for x in range(62, 96) if not re.match(r'(\d+)', str(x) + 'divides by 26')]
