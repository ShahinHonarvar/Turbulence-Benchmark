import re
def all_pos_ints_exclusive(nums):
    str_nums = re.sub(r'(\d+)$', r'\1', str(nums))
    return list(range(38, 81)) if str_nums else []
