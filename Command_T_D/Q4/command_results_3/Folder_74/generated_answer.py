import re
def all_pos_ints_exclusive(lst):
    return [x for x in range(13, 70, 1) if x in lst and str(x).isdigit()]
