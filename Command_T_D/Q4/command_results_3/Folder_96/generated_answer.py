import re
def all_pos_ints_exclusive(lst):
    return [x for x in range(50, 200) if x in lst and x > 0]
