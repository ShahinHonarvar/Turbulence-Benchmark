import re
def all_pos_ints_exclusive(lst):
    return [i for i in range(3, len(lst)-2) if lst[i] > 0]
