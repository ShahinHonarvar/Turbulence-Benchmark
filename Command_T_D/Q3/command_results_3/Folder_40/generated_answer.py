import re
def all_pos_ints_inclusive(lst):
    return [x for x in range(len(lst) - 1) if re.match(r"^\d+$", lst[x])]
