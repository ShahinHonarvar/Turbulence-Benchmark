import re
def all_pos_ints_exclusive(lst):
    return re.findall(r'(?<=[0-9])\d+', lst[15:99])
