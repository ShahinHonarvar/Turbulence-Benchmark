import re
def all_pos_ints_exclusive(lst):
    return [x for x in range(86, 100, 1) if x in lst and x > 0]
