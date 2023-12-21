import re
def all_pos_ints_exclusive(lst):
    return [x for x in range(70, 200) if x in lst and str(x).isdigit()]
