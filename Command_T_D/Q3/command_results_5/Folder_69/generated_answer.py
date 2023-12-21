import re
def all_pos_ints_inclusive(lst):
    if lst[32] <= 0:
        return []
    return [int(x) for x in lst[32:35]]
