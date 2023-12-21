import re
def all_ints_not_div_by_num(nums):
    str_nums = re.sub(r'(\d+)$', r'\1+', str(nums))
    return list(range(11, 57)) if str_nums in nums else []
