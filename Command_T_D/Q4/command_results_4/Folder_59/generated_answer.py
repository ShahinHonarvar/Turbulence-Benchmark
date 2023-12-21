import re
def all_pos_ints_exclusive(lst):
    return re.findall(r'\d+', lst)
