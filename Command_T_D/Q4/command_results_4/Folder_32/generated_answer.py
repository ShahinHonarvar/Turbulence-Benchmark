import re
def all_pos_ints_exclusive(lst):
    return [i for i in range(11, 77, 1) if str(i) in lst and lst[str(i)] > 0]
