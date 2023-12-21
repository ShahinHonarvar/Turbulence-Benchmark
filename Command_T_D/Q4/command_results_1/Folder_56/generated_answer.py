import re
def all_pos_ints_exclusive(nums):
    return re.findall(r'\d+', str(nums)[7:-1])
