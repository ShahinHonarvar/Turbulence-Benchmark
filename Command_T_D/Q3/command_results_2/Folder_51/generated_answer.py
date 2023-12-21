import re
def all_pos_ints_inclusive(lst):
    return [i for i in range(1, 9) if str(i) in lst]
