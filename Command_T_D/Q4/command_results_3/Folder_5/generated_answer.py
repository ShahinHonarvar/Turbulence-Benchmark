import re
def all_pos_ints_exclusive(lst):
    return [i for i in range(2, len(lst) + 1) if re.match(r'\d+', lst[i])]
